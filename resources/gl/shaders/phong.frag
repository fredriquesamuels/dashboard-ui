
precision mediump float;
varying vec2 vTextureCoord;
varying vec3 vLightWeighting;
uniform sampler2D texture0;
void main(void) {
    vec4 textureColor = vec4(1.0,1.0,1.0,1.0);//texture2D(texture0, vec2(vTextureCoord.s, vTextureCoord.t));
    gl_FragColor = vec4(textureColor.rgb * vLightWeighting, textureColor.a);
}
