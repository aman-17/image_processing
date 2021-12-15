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

#pragma transparent

#pragma body

float3 tintColor = pow(float3(0.800, 0.506, 0.108), 2.3);

float3 in_min = .05;
float3 in_max = .95;
float3 out_min = 0.15;
float3 out_max = 0.95;
float3 remap_diffuse = out_min + (out_max - out_min) * (_surface.diffuse.rgb - in_min)/(in_max - in_min);

float3 tintHsv = rgb2hsv(tintColor);
float3 hsvInput = rgb2hsv(remap_diffuse);
_surface.diffuse.rgb = hsv2rgb(float3(tintHsv.r, (1.0 - hsvInput.b) * 1.6, hsvInput.b)) * _surface.diffuse.a;
