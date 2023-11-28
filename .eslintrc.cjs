/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
  root: true,
  extends: [
    'plugin:vue/vue3-essential',
    // 'eslint:recommended',
    '@vue/eslint-config-typescript',
    // '@vue/eslint-config-prettier/skip-formatting'
  ],
  rules: {
    // 声明了没用就别给我报错啦！
    '@typescript-eslint/no-unused-vars': 'off',
    //  关了any警告
    '@typescript-eslint/no-explicit-any': 'off',
    // 驼峰命名也别报错
    'vue/multi-word-component-names': 0,
    // 忘了这是啥了
    '@typescript-eslint/no-non-null-assertion': 'off',
  },

  overrides: [
    {
      files: ['cypress/e2e/**/*.{cy,spec}.{js,ts,jsx,tsx}'],
      extends: ['plugin:cypress/recommended'],
    },
  ],
  parserOptions: {
    ecmaVersion: 'latest',
  },
};
