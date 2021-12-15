_surface.diffuse = pow(float4(0.854, 0.722, 0.482, 1.0), 2.3);
_surface.emission = pow(float4(0.768, 0.647, 0.431, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.700, 0.532, 0.245, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.5, 3, 0.009, 10);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.0, 0.0, 0.0);
