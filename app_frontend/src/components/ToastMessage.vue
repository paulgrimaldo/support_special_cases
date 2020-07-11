<template>
  <div aria-live="polite" aria-atomic="true" style="position: fixed;">
    <div :id="id" class="toast" role="alert" data-autohide="false">
      <div class="toast-header">
        <img src="../assets/support_logo.svg" width="48px" height="48px" alt="Support Ficct"/>
        <strong class="mr-auto" v-html="title"></strong>
        <small v-html="when"></small>
        <button
          type="button"
          class="ml-2 mb-1 close"
          data-dismiss="toast"
          aria-label="Close"
          @click="$emit('clickCloseToast')"
        >
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="toast-body" v-html="content"></div>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      title: {
        type: String,
        required: false,
        default: 'Support Ficct'
      },
      when: {
        type: String,
        required: false,
        default: 'Justo ahora'
      },
      content: {
        type: String,
        required: true
      },
      id: {
        type: String,
        required: true,
        default: 'toast-content'
      }
    }
  }
</script>

<style scoped>

</style>
