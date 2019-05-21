<template>
  <div class="auth">
    <Auth/>
  </div>
</template>

<script>
// @ is an alias to /src
import Auth from '@/components/Auth.vue'

export default {
  name: 'login',
  components: {
    Auth
  }
}
</script>