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
          <router-link v-if="getCookieMethod()" to="/auth/login/"><span>ВЫЙТИ</span></router-link>
          <router-link v-else to="/auth/logout/"><span>ВОЙТИ</span></router-link>
          <router-link to="/auth/register/">
            <button class="regBtnTitle ">РЕГИСТРАЦИЯ</button>
          </router-link>
        </div>
        <div class="col-1 p-0"></div>
      </div>
    </div>
    <div class="profileGiftsInfo d-flex">
      <div class="col-1 p-0 m-0">
        <div class="GiftsNavIcons d-flex flex-column p-0">
          <div class="profileGiftNavIcon d-flex p-0 m-0 justify-content-center align-items-center">
            <img src="../../public/static/images/house_icon.svg" alt="1.jpg">
          </div>
          <div class="profileGiftNavIcon d-flex p-0 m-0 justify-content-center align-items-center">
            <img src="../../public/static/images/friends_icon.png" alt="1.jpg">
          </div>
        </div>
      </div>
      <div class="col-3 p-0">
        <div class="userEditDataProfile">
          <div class="userEditItemImg"></div>
          <div class="userEditItemName text-center">
            <div class="userEditItemNameText">
              <span class="text-uppercase">{{userInfo.last_name}}</span><br/>
              <span>{{userInfo.first_name}}</span>
            </div>
            <router-link to="/profile_put/">
              <img class="userEditItemNameTextCloud" src="../../public/static/images/edit_white.svg" alt="1.jpg">
            </router-link>
          </div>
        </div>
      </div>
      <div class="col-1 p-0"></div>
      <div class="col-6 p-0">
        <div class="profileGiftLogin text-left"><span>{{userInfo.login}}</span></div>
        <div class="profileGiftBirthdate text-left"><span>{{userInfo.birthdate}}</span></div>
        <div class="profileGiftGifts w-100 d-flex justify-content-between">
          <div v-for="gift in gifts.slice(0, 2)" v-bind:key="gift.id" class="profileGiftGiftsItem">
            <div class="GiftsInfo">
              <div><img src="../../public/static/images/clock_img.svg" alt="1.jpg"></div>
              <div><span>{{gift.name}}</span></div>
            </div>
            <div class="GiftsButton d-flex justify-content-center align-items-center">СМОТРЕТЬ</div>
          </div>
          <div class="profileGiftGiftsItem">
            <div style="padding-top: 63px;" data-toggle="modal" data-target=".bd-example-modal-lg" class="GiftsButton m-0 GiftsInfo d-flex justify-content-center">СОЗДАТЬ</div>
            <div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
              <div class="modal-dialog modal-lg">
                <div class="modal-content">
                  <div class="container-fluid p-0 text-center giftCreationForm">
                    <div class="giftCreationHeader">
                      <span>ПОЖЕЛАНИЕ</span>
                    </div>
                    <div class="giftCreationInfo d-flex">
                      <div class="col-1 p-0"></div>
                      <div class="col-3 p-0 d-flex flex-column">
                        <div class="giftCard d-flex flex-column justify-content-between">
                          <img class="d-flex w-100" src="../../public/static/images/giftCreationForm/giftImg.svg" alt="no image">
                          <a href="#">
                            <img src="../../public/static/images/giftCreationForm/cloud.svg" alt="">
                          </a>
                        </div>
                        <div class="giftInfoPrice d-flex">
                          <input v-model="giftInfo.price" class="w-100" placeholder="Цена:" type="text">
                        </div>
                        <button v-on:click="createGift">СОЗДАТЬ</button>
                      </div>
                      <div class="col-1 p-0"></div>
                      <div class="col-6 p-0 d-flex flex-column giftInfoPrice m-0">
                        <input v-model="giftInfo.name" class="giftCreationName" placeholder="Название:" type="text">
                        <input class="giftCreationUrl" placeholder="Ссылка:" type="text">
                        <textarea v-model="giftInfo.description" class="giftCreationDesc" placeholder="Описание:"></textarea>
                        <div class="giftCreationCollection">
                          <div class="collectionHeader">Коллекция:</div>
                          <div class="collectionImages d-flex justify-content-between">
                            <div class="d-flex">
                              <img class="m-auto" src="../../public/static/images/giftCreationForm/icon1.svg" alt="">
                            </div>
                            <div class="d-flex">
                              <img class="m-auto" src="../../public/static/images/giftCreationForm/icon2.svg" alt="">
                            </div>
                            <div class="d-flex">
                              <img class="m-auto" src="../../public/static/images/giftCreationForm/icon3.svg" alt="">
                            </div>
                            <div class="d-flex">
                              <img class="m-auto" src="../../public/static/images/giftCreationForm/icon4.svg" alt="">
                            </div>
                            <div class="d-flex">
                              <img class="m-auto" src="../../public/static/images/giftCreationForm/icon5.svg" alt="">
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="col-1 p-0"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-1 p-0"></div>
    </div>
    <div class="myGiftsHeader text-left d-flex">
      <div class="col-1"></div>
      <div class="col-10">
        <span>Мои пожелания:</span>
      </div>
      <div class="col-1"></div>
    </div>
    <div class="myGiftsGroups d-flex">
      <div class="col-1"></div>
      <div class="col-10 giftsGroupsBtns d-flex justify-content-center">
        <div style="background: #DC4E41;" class="giftGroupBtn d-flex justify-content-center align-items-center">
          <span>Все</span>
        </div>
        <div style="background: rgba(101, 187, 94, 0.5);" class="giftGroupBtn d-flex justify-content-center align-items-center">
          <img src="../../public/static/images/mini-house.svg" alt="1.jpg">
          <span>Дом</span>
        </div>
        <div style="background: rgba(90, 102, 209, 0.5);" class="giftGroupBtn d-flex justify-content-center align-items-center">
          <img src="../../public/static/images/mini-portfolio.svg" alt="1.jpg">
          <span>Работа</span>
        </div>
        <div style="background: rgba(127, 43, 193, 0.5);" class="giftGroupBtn d-flex justify-content-center align-items-center">
          <img src="../../public/static/images/mini-photo-camera.svg" alt="1.jpg">
          <span>Хобби</span>
        </div>
        <div style="background: rgba(83, 84, 82, 0.5);" class="giftGroupBtn d-flex justify-content-center align-items-center">
          <img src="../../public/static/images/mini-car-compact.svg" alt="1.jpg">
          <span>Машина</span>
        </div>
      </div>
      <div class="col-1"></div>
    </div>
    <div class="myGiftsInGroup d-flex">
      <div class="col-1"></div>
      <div class="col-1 d-flex justify-content-center align-items-center">
        <img src="../../public/static/images/to-left.svg" alt="1.jpg">
      </div>
      <div class="col-8 d-flex justify-content-between">
        <div v-for="gift in gifts.slice(0, 3)" v-bind:key="gift.id" class="giftItemInGroup d-flex">
          <div class="giftItemInfo">
            <div class="giftItemImg"><img src="../../public/static/images/big_clock.svg" alt="1.jpg"></div>
            <div class="giftItemName text-left">{{gift.name}}</div>
            <div class="giftItemPrice text-left d-flex p-0 justify-content-between">
              <span>{{gift.price}}</span>
              <img src="../../public/static/images/mini-info.svg" alt="1.jpg">
              <img src="../../public/static/images/mini-edit.svg" alt="1.jpg">
            </div>
          </div>
          <div class="giftItemDelete">
            <img src="../../public/static/images/mini-delete.svg" alt="1.jpg">
          </div>
        </div>
      </div>

      <div class="col-1 d-flex justify-content-center align-items-center">
        <img src="../../public/static/images/to-right.svg" alt="1.jpg">
      </div>
    </div>
    <div class="col-1"></div>
    <div class="giftIconNav d-flex justify-content-center">
      <div></div>
      <div></div>
      <div></div>
    </div>
    <div class="giftCreate">
      <div class="text-center">
        <span>Создайте новое пожелание!</span>
      </div>
      <div class="giftCreateBtn d-flex justify-content-center align-items-center m-auto">СОЗДАТЬ</div>
    </div>
  </div>
</template>

<script>
	import {Gifts} from "../api/gifts";
	import {Profile} from '../api/profile';

	function getCookie(name) {
		let a = document.cookie.split('; ');
		for (let c in a) {
			let tmp = a[c].split('=');
			if (name === tmp[0]) {
				return (Number(tmp[1]));
			}
		}
	}

	export default {
		name: "Profile_GIFT",
		data () {
			return {
				"userId": Number,
				"gifts": [],
				"userInfo": {},
				"giftInfo": {
					"name": null,
					"description": null,
					"price": null,
				}
			}
		},
		methods: {
			getGifts() {
				Gifts.read().then(response => {
					for(let c of response) {
						if (this.userId === c.user) {
							this.gifts.push(c)
						}
					}
				})
			},
			profileGet() {
				Profile.read({'id': this.userId,}).then(response => {
					this.userInfo = response
				})
			},
			getCookieMethod() {
				return getCookie('userId')
			},
			createGift() {
				Gifts.post({
					"user": this.userId,
					"name": this.giftInfo.name,
					"description": this.giftInfo.description,
					"price": this.giftInfo.price
				})
				this.giftInfo.name = null;
				this.giftInfo.description = null;
				this.giftInfo.price = null;
			}
		},
		mounted() {
			this.getGifts();
			this.userId = getCookie('userId');
			this.profileGet();
		}
	}
</script>

<style scoped>

</style>