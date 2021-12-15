#pragma arguments
float vertical_offsetv;

#pragma body

float offset = 3.1 + vertical_offsetv;
float3 pos = (scn_node.modelTransform * _geometry.position).xyz;
pos.y /= 4.0;
pos.y -= offset;

float mask = mix(0.0, 3.0, saturate(pos.y));
float3 pushOut = normalize(float3(_geometry.position.x, 0.0, _geometry.position.z));
_geometry.position.xz += pushOut.xz * mask * float2(0.5, 1.0);
