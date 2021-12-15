#pragma transparent

#pragma arguments
texture2d mask_texture;

#pragma body
constexpr sampler textureSampler(coord::normalized, address::clamp_to_edge, filter::linear, min_filter::linear, mag_filter::linear);
constexpr sampler textureSamplerMip(coord::normalized, address::clamp_to_edge, filter::linear, min_filter::linear, mag_filter::linear, mip_filter::linear);

float offset = 3.1;
float3 point = (scn_frame.inverseViewTransform * float4(_surface.position.xyz, 1.0)).xyz;
point.xy /= float2(40,4);
point.y -= offset;

float X = -point.x;
float Y = -point.y;
X *= sign(point.z);
float2 UV = float2(X + 0.5,Y + 1.0); 

float mask = mask_texture.sample(textureSampler, UV).r;
if (mask<0.9) discard_fragment();
