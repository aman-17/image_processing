_surface.diffuse = pow(float4(0.929, 0.894, 0.898, 1.0), 2.3);
_surface.emission = pow(float4(0.533, 0.518, 0.518, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.316, 0.337, 0.354, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(1.0, 1.0, 0, 0);
// SpecularColor
_surface.multiply = float4(1.0, 0.92, 0.9, 1.0);
// Wrap
_surface.specular = float4(0.0, 0.3, -8, 0.0);
