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
            <button class="navbar-toggler" type="button" data-toggle="collapse"
                    data-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent"
                    aria-expanded="false" aria-label="Toggle navigation">
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
          <router-link to="/auth/login/"><span>ВОЙТИ</span></router-link>
          <button class="regBtnTitle">РЕГИСТРАЦИЯ</button>
        </div>
        <div class="col-1 p-0"></div>
      </div>
    </div>
    <div class="container">
      <div class="row userEditData">
        <div class="col-xl-1"></div>
        <div class="col-xl-3 text-center">
          <div class="userEditDataProfile">
            <div class="userEditItemImg"></div>
            <div class="userEditItemName text-center">
              <div class="userEditItemNameText">
                <span class="text-uppercase">{{last_name}}</span><br/>
                <span>{{first_name}}</span>
              </div>
              <img class="userEditItemNameTextCloud" src="../../public/static/images/cloud.svg">
            </div>
          </div>
        </div>
        <div class="col-xl-2"></div>
        <div class="col-xl-5">
          <div class="row userEditDataData">
            Основные данные
          </div>
          <div class="row userEditDataDataProfType">
            Имя: {{first_name}}
          </div>
          <div class="row userEditDataDataProfType">
            Фамилия: {{last_name}}
          </div>
          <div class="row userEditDataDataProfType">
            Логин: {{login}}
          </div>
          <div class="row userEditDataDataProfType">
            E-mail: {{email}}
          </div>
          <div class="row userEditDataDataProfType">
            Телефон: {{phone}}
          </div>
          <div class="row userEditDataDataProfType">
            Дата рождения: {{birthdate}}
          </div>
          <div class="row userEditDataDataProfType">
            Пол: {{gender}}
          </div>
        </div>
        <div class="col-xl-1"></div>
      </div>
      <div class="row userEditDataSecond">
        <div class="col-xl-1"></div>
        <div class="col-xl-10 userEditDataData">
          Адрес:
        </div>
        <div class="col-xl-1"></div>
      </div>
      <div class="row userEditDataThird">
        <div class="col-xl-1"></div>
        <div class="col-xl-10">
          <div class="row">
            <div class="col-xl-3 userEditDataDataProfType">Страна: {{country}}</div>
            <div class="col-xl-1 userEditDataDataProfType"></div>
            <div class="col-xl-4 userEditDataDataProfType">Регион: {{region}}</div>
            <div class="col-xl-1 userEditDataDataProfType"></div>
            <div class="col-xl-3 userEditDataDataProfType">Город: {{city}}</div>
          </div>
          <div class="row col-xl-12 userEditDataDataProfType">
            Адрес: {{street}}, дом: {{building}}, корпус: , квартира: {{flat}}, индекс: 333444
          </div>
        </div>
        <div class="col-xl-1"></div>
      </div>
      <div class="row userEditDataSecond">
        <div class="col-xl-1"></div>
        <div class="col-xl-10 userEditDataData">
          Приватность:
        </div>
        <div class="col-xl-1"></div>
      </div>
      <div class="row userEditDataForth">
        <div class="col-xl-1"></div>
        <div class="col-xl-10">
          <div class="row col-xl-12 userEditDataDataProfType">
            Тип профиля: открытый
          </div>
          <div class="row col-xl-12 userEditDataDataProfType">
            Уведомления и оповещения: доступны
          </div>
        </div>
        <div class="col-xl-1"></div>
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
	import {Profile} from "../api/profile";

	export default {
		name: "Profile_GET",
		data() {
			return {
				"id": this.$root.$data.userId,
				"first_name": '',
				"middle_name": '',
				"last_name": '',
				"birthdate": '',
				"gender": '',
				"phone": '',
				"avatar": '',
				"login": '',
				"email": '',
				"country": '',
				"region": '',
				"city": '',
				"street": '',
				"building": '',
				"flat": ''
			}
		},
		methods: {
			submitForm() {
				this.profileGet()
			},
			profileGet() {
				Profile.read({'id': this.id}).then(response => {
					this.first_name = response.first_name;
          this.middle_name = response.middle_name;
          this.last_name = response.last_name;
          this.birthdate = response.birthdate;
          this.gender = response.gender;
          this.phone = response.phone;
          this.avatar = response.avatar;
          this.login = response.login;
          this.email = response.email;
          this.country = response.country;
          this.region = response.region;
          this.city = response.city;
          this.street = response.street;
          this.building = response.building;
          this.flat = response.flat;
				})
			}
		},
    beforeMount() {
			this.profileGet()
    }
	}
</script>

<style scoped>

</style>