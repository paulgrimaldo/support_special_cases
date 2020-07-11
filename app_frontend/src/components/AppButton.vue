<template>
  <button type="button" class="btn btn-dark" @click="$emit('click')">
    <slot></slot>
  </button>
</template>

<script>
  export default {}
</script>

<style scoped>

</style>
