{
  'variables': {
    'platform': '<(OS)',
  },
  'conditions': [
    # Replace gyp platform with node platform, blech
    ['platform == "mac"', {'variables': {'platform': 'darwin'}}],
    ['platform == "win"', {'variables': {'platform': 'win32'}}],
  ],
  'targets': [
    {
      #'target_name': 'glfw-<(platform)-<(target_arch)',
      'target_name': 'node-glfw',
      'defines': [
        'VERSION=0.1.1'
      ],
      'sources': [ 'src/atb.cc', 'src/glfw.cc' ],
      'include_dirs': [
        '$(HOME)/code/AntTweakBar/include',
      ],
      'conditions': [
        ['OS=="linux"', {'libraries': ['-lAntTweakBar', '-lglfw', '-lGLEW']}],
        ['OS=="mac"', {'libraries': ['-lAntTweakBar', '-lglfw', '-lGLEW', '-framework OpenGL']}],
        ['OS=="win"', {'libraries': [
            'AntTweakBar64.lib',
            'glew32s.lib', 
            'glfwdll.lib', 
            'opengl32.lib'
            ]
          }
        ],
      ],
    }
  ]
}