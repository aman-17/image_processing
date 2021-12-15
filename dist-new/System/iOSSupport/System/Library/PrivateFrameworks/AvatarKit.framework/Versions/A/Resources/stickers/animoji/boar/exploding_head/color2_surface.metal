_surface.diffuse = pow(float4(0.611, 0.459, 0.380, 1.0), 2.3);
_surface.emission = pow(float4(0.329, 0.224, 0.169, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.492, 0.360, 0.187, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.0, 3.0, 0.0, 0);
// SpecularColor
_surface.multiply = float4(0.9, 0.7, 0.5, 1.0);
// Wrap
_surface.specular = float4(0.5, 0.0, 0.0, 0.0);
