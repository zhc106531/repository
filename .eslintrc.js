// module.exports = {
//   root: true,
//   env: {
//     node: true
//   },
//   'extends': [
//     'plugin:vue/vue3-essential',
//     'eslint:recommended',
//     '@vue/typescript/recommended'
//   ],
//   parserOptions: {
//     ecmaVersion: 2020
//   },
//   rules: {
//     'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
//     'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off'
//   }
// }


module.exports = {
  root: true,
  env: {
    // browser: true
    // es6: true,
    node: true
  },
  // parser: 'vue-eslint-parser',
  extends: [
    'plugin:vue/vue3-essential',
    // 'eslint:recommended',
    '@vue/typescript/recommended'
    // 'plugin:prettier/recommended'
  ],
  parserOptions: {
    ecmaVersion: 2020
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    // 关闭驼峰命名规则
    'vue/multi-word-component-names': 0,
    '@typescript-eslint/no-unused-vars': 'off',
    // 关闭any警告
    '@typescript-eslint/no-explicit-any': 'off',
    //
    '@typescript-eslint/no-non-null-assertion': 'off',
    //关闭没有返回的检测
    //  '@typescript-eslint/explicit-module-boundary-types': 'off'

  }
}
