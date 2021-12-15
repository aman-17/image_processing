_surface.diffuse = pow(float4(0.635, 0.718, 0.239, 1.0), 2.3);
_surface.emission = pow(float4(0.408, 0.498, 0.176, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.581, 0.792, 0.016, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.0, 0.0, 0.0, 0);
// SpecularColor
_surface.multiply = float4(0.5, 0.3, 0.0, 1.0);
// Wrap
_surface.specular = float4(-0.1, 0.0, 0.0, 0.0);
