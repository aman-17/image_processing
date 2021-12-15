_surface.diffuse = pow(float4(0.929, 0.894, 0.851, 1.0), 2.3);
_surface.emission = pow(float4(0.647, 0.494, 0.310, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = float4(1.0, 1.0, 1.0, 1.0);
// edgeDark_rimLight
_surface.reflective = float4(0, 0, 0.05, 0);
// SpecularColor
_surface.multiply = float4(0.2, 0.2, 0.2, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, 0.0, 0.0);
