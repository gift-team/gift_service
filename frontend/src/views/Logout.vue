<template>
  <div class="auth">
    <Auth/>
  </div>
</template>

<script>
	import Auth from '../components/Auth';
  import setCookie from '../components/Auth'
	export default {
		name: 'Logout',
    components: {
			Auth
    },
    beforeMount() {
			setCookie('userId', '', {expires: -1})
    }
	};
</script>

<style scoped>

</style>