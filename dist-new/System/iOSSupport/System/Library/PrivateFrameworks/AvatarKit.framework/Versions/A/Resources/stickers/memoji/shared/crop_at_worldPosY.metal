#pragma transparent

#pragma arguments
float crop_pos;

#pragma body
float3 world_space_pos = (scn_frame.inverseViewTransform * float4(_surface.position.xyz, 1.0)).xyz;
if (1.0 - step(crop_pos,world_space_pos.y)) discard_fragment();
