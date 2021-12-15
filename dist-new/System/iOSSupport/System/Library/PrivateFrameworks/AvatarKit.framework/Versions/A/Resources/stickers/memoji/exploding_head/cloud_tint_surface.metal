static float3 rgb2hsv(float3 c)
{
    float4 K = float4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    float4 p = mix(float4(c.bg, K.wz), float4(c.gb, K.xy), step(c.b, c.g));
    float4 q = mix(float4(p.xyw, c.r), float4(c.r, p.yzx), step(p.x, c.r));
    
    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return float3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

static float3 hsv2rgb(float3 c)
{
    float4 K = float4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    float3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

// color manipulation
static float3 colormanipAMM(float3 color, float h, float s, float v){
    float3 specular_hsv = rgb2hsv(color);
    return hsv2rgb(float3(specular_hsv.x + h, specular_hsv.y * s, specular_hsv.z * v));
}

#pragma transparent
#pragma arguments
float4 shadowhsv;
float4 specularhsv;

#pragma body
//// VARIABLES ////
float h;
float s;
float v;
float m;

//// LIGHT ////
float smoothedlight = _surface.emission.r;

//// DIFFUSE ////
float diffuse =  smoothedlight;

// color shadows skin
h = shadowhsv.x;
s = shadowhsv.y;
v = shadowhsv.z;
m = 1.0 - diffuse;
float3 skinColor = mix(_surface.diffuse.rgb, colormanipAMM(_surface.diffuse.rgb, h, s, v), m);

float3 hsvSkin = rgb2hsv(skinColor);
float3 hsvInput = rgb2hsv(_surface.emission.rgb);
_surface.diffuse = float4(hsv2rgb(float3(hsvSkin.r, (1.0 - hsvInput.b) * 0.5, hsvInput.b)), 1.0);

_surface.diffuse.a = _surface.emission.a;
_surface.diffuse.rgb *= _surface.diffuse.a;

_surface.multiply = 1.0;
_surface.emission = 0.0;
