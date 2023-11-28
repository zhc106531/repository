<template>
  <div id="app">
    <!-- <router-view name="header" />  -->
    <div class="main-container">
      <!-- <router-view name="MultiWordSidebar" /> -->
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
/* Add your global styles here */
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main-container {
  display: flex;
}
</style>
