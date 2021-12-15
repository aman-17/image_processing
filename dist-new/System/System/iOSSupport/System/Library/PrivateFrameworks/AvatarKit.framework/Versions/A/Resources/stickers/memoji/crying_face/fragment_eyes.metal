float2 uv = _surface.diffuseTexcoord;
uv = uv*2.0 - 1.0;
float pi = 3.141592;
float r_big = .225;
float hl_big = smoothstep(1. - r_big + sin(scn_frame.time * pi * 6) * 0.02,
                          1. - r_big + sin(scn_frame.time * pi * 10) * 0.02 + .05,
                          1.0 - length(uv - float2(
                                                   -0.15 + sin(scn_frame.time * pi * 8) * 0.015,
                                                   -0.15 + sin(scn_frame.time * pi * 12) * 0.012)));

float r_small = .075;
float hl_small = smoothstep(1. - r_small + sin(scn_frame.time * pi * 8) * 0.01,
                            1. - r_small + sin(scn_frame.time * pi * 6) * 0.01 + .05,
                            1.0 - length(uv - float2(
                                                     0.175 + sin(scn_frame.time * pi * 10) * 0.008,
                                                     0.175 + sin(scn_frame.time * pi * 14) * 0.01)));

_output.color.rgb += hl_big * 1.0 + hl_small * 0.9;
