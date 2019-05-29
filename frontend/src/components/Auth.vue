<template>
  <div class="container-fluid p-0 text-center">
    <div class="title">
      <div class="titleMenu d-lg-flex">
        <div class="pos-f-t d-sm-none">
          <div class="collapse" id="navbarToggleExternalContent">
            <div class="bgNav">
              <ul class="navbar-nav navGroup">
                <li class="nav-item">
                  <a class="nav-link" href="#">ПОЖЕЛАНИЯ</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">ВОЙТИ</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">РЕГИСТРАЦИЯ</a>
                </li>
              </ul>
            </div>
          </div>
          <nav class="navbar navbar-light bgNav">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
          </nav>
        </div>
        <div class="col-1 p-0"></div>
        <div class="w-100 logoTitle col-lg-4 col-12 d-flex p-0">
          <router-link to="/"><img src="../../public/static/images/LOGO.svg" alt=""></router-link>
        </div>
        <div class="menu col-lg-6 col-12 justify-content-between d-flex align-items-center p-0">
          <span>ПОЖЕЛАНИЯ</span>
          <span>ВОЙТИ</span>
          <router-link to="/auth/register/"><button class="regBtnTitle ">РЕГИСТРАЦИЯ</button></router-link>
        </div>
        <div class="col-1 p-0"></div>
      </div>
    </div>
    <div class="registration authentication pt-5 pb-5">
      <div class="regHeader">
        <p>ВХОД</p>
      </div>
      <div class="regForm d-flex">
        <div class="col-3 p-0"></div>
        <form @submit="submitLoginForm()" class="text-center col-6 p-0" action="#">
          <!--<input placeholder="Имя:" class="email col-12" type="text">-->
          <!--<input placeholder="Фамилия:" class="email col-12" type="text">-->
          <input v-model="login" placeholder="E-mail:" class="email col-12" type="text">
          <input v-model="pass" placeholder="Пароль:" class="password1 col-12" type="password">
          <!--<input placeholder="Повторите пароль:" class="password2 col-12" type="password">-->
          <div class="custom-control custom-checkbox">
            <input type="checkbox" class="custom-control-input" id="customCheck1">
            <label class="custom-control-label" for="customCheck1">Подтверждаю обработку персональных данных</label>
          </div>
          <div class="lendBts p-0 col-12 flex-column flex-md-row d-flex justify-content-md-between align-items-center">
            <button class="regBtnTitle">ВХОД</button>
            <div class="col-12 col-md-4 p-2 p-md-0 d-flex justify-content-end">
              <a class="m-1" href="#">
                <img src="../../public/static/images/VK.svg" alt="">
              </a>
              <a class="m-1" href="#">
                <img src="../../public/static/images/G+.svg" alt="">
              </a>
            </div>
          </div>
        </form>
        <div class="col-3 p-0"></div>
      </div>
    </div>
    <div class="footer p-0 m-auto m-sm-0 d-md-flex">
      <div class="col-1 p-0"></div>
      <div class="col-4 p-0">
        <div class="left d-flex flex-column">
          <div class="imgFooter d-none d-lg-flex">
            <img src="../../public/static/images/LOGO.svg" alt="">
          </div>
          <div class="copyright">&copy; 2018-2019 «GiftService»</div>
        </div>
      </div>
      <div class="col-3 p-0"></div>
      <div class="col-3 p-0 d-flex align-items-center">
        <div class="right d-flex flex-column align-items-center w-100">
          <div class="footerMenu col-12 float-right justify-content-between d-inline-block d-md-flex">
            <p class="m-0">О НАС</p>
            <p class="m-0">КОНТАКТЫ</p>
            <p class="m-0">ОТЗЫВЫ</p>
          </div>
          <div class="footerBottom p-0 col-12 d-flex justify-content-end">
            <img class="" src="../../public/static/images/instagram.svg" alt="">
            <img class="" src="../../public/static/images/facebook.svg" alt="">
          </div>
        </div>
      </div>
      <div class="col-1 p-0"></div>
    </div>
  </div>
</template>

<script>
	import {Users} from "../api/users";
	// import Profile_GET from './Profile_GET';
	// let USER_ID = 0;

	export default {
		name: "auth",
		data () {
			return {
				'login': '',
				'pass': '',
				'd': null
			}
		},
		methods: {
			submitLoginForm () {
				this.loginUser();
				this.login = '';
				this.pass = '';
			},
			loginUser () {
				Users.login({'email': this.login, 'password': this.pass}).then(response => {
					this.$root.$data.userId = response.id
          this.setCookie('userId', response.id, {expires: 3600, path: '/'})
					return this.$router.push({name: 'profile_get'})
				})
			},
			setCookie(name, value, options) {
				options = options || {};

				let expires = options.expires;

				if (typeof expires == "number" && expires) {
					let d = new Date();
					d.setTime(d.getTime() + expires * 1000);
					expires = options.expires = d;
				}
				if (expires && expires.toUTCString) {
					options.expires = expires.toUTCString();
				}

				value = encodeURIComponent(value);

				let updatedCookie = name + "=" + value;

				for (let propName in options) {
					updatedCookie += "; " + propName;
					let propValue = options[propName];
					if (propValue !== true) {
						updatedCookie += "=" + propValue;
					}
				}

				document.cookie = updatedCookie;
			}
		},
	}
</script>
