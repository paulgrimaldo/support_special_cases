<template>
  <div id="app">
    <the-navbar/>
    <main class="container mt-5">
      <router-view/>
    </main>
    <the-footer/>
  </div>
</template>

<script>
  export default {
    name: "App"
  };
</script>
<style>
</style>
