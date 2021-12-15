_surface.diffuse = pow(float4(0.961, 0.961, 0.957, 1.0), 2.3);
_surface.emission = pow(float4(0.604, 0.604, 0.608, 1.0), 2.3);
// EdgesDarkeningColor
_surface.ambient = pow(float4(0.315, 0.456, 0.621, 1.0), 2.3);
// edgeDark_rimLight
_surface.reflective = float4(0.6, 2.5, 0, 4);
// SpecularColor
_surface.multiply = float4(1.0, 1.0, 1.0, 1.0);
// Wrap
_surface.specular = float4(0.5, -0.1, 0.0, 0.0);
