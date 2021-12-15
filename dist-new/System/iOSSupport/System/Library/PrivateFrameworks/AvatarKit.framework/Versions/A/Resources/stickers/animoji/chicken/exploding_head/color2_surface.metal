_surface.diffuse = pow(float4(0.923, 0.334, 0.314, 1.0), 2.3);
_surface.emission = pow(float4(0.896, 0.220, 0.184, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = float4(1.0, 1.0, 1.0, 1.0);
// edgeDark_rimLight
_surface.reflective = float4(0, 0, 0.01, 0);
// SpecularColor
_surface.multiply = float4(0.8, 0.8, 0.8, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, 0.0, 0.0);
