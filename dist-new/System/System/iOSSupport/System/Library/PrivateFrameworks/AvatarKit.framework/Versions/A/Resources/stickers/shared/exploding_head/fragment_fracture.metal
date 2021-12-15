#pragma transparent

#pragma arguments
texture2d mask_texture;
texture2d maskshadow_texture;
float vertical_offsetf;
//float4 shadowhsv;

#pragma body
constexpr sampler textureSampler(coord::normalized, address::clamp_to_edge, filter::linear, min_filter::linear, mag_filter::linear);
constexpr sampler textureSamplerMip(coord::normalized, address::clamp_to_edge, filter::linear, min_filter::linear, mag_filter::linear, mip_filter::linear);

float offset = 3.1 + vertical_offsetf;
float3 point = (scn_frame.inverseViewTransform * float4(_surface.position.xyz, 1.0)).xyz;
point.xy /= float2(40,4);
point.y -= offset;

float X = -point.x;
float Y = -point.y;
X *= sign(point.z);
float2 UV = float2(X + 0.5,Y + 1.0); 

float mask = mask_texture.sample(textureSampler, UV).r;
if (mask<0.9) discard_fragment();

float maskshadow = 1. - abs(0.5 - maskshadow_texture.sample(textureSampler, UV).r) * 2;
//float maskshadow = maskshadow_texture.sample(textureSampler, UV).r;

_output.color.rgb = mix(_output.color.rgb, _output.color.rgb * 0.2, maskshadow);
