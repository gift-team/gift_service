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
          <span>ВОЙТИ</span>
          <router-link to="/auth/register/">
            <button class="regBtnTitle ">РЕГИСТРАЦИЯ</button>
          </router-link>
        </div>
        <div class="col-1 p-0"></div>
      </div>
    </div>
    {{gifts}}
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
              <span class="text-uppercase">{{last_name}}</span><br/>
              <span>{{first_name}}</span>
            </div>
            <img class="userEditItemNameTextCloud" src="../../public/static/images/edit_white.svg" alt="1.jpg">
          </div>
        </div>
      </div>
      <div class="col-1 p-0"></div>
      <div class="col-6 p-0">
        <div class="profileGiftLogin text-left"><span>{{login}}</span></div>
        <div class="profileGiftBirthdate text-left"><span>{{birthdate}}</span></div>
        <div class="profileGiftGifts w-100 d-flex justify-content-between">
          <div class="profileGiftGiftsItem">
            <div class="GiftsInfo">
              <div><img src="../../public/static/images/clock_img.svg" alt="1.jpg"></div>
              <div><span>ЧАСЫ</span></div>
            </div>
            <div class="GiftsButton d-flex justify-content-center align-items-center">СМОТРЕТЬ</div>
          </div>
          <div class="profileGiftGiftsItem">
            <div class="GiftsInfo">
              <div><img src="../../public/static/images/clock_img.svg" alt="1.jpg"></div>
              <div><span>ЧАСЫ</span></div>
            </div>
            <div class="GiftsButton d-flex justify-content-center align-items-center">СМОТРЕТЬ</div>
          </div>
          <div class="profileGiftGiftsItem">
            <div style="padding-top: 63px;" class="GiftsButton m-0 GiftsInfo d-flex justify-content-center">СОЗДАТЬ</div>
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
      <div class="col-10 giftsGroupsBtns d-flex">
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
<!--        <div class="giftItemInGroup d-flex">-->
<!--          <div class="giftItemInfo">-->
<!--            <div class="giftItemImg"><img src="../../public/static/images/big_clock.svg" alt="1.jpg"></div>-->
<!--            <div class="giftItemName text-left">{{name}}</div>-->
<!--            <div class="giftItemPrice text-left d-flex p-0 justify-content-between">-->
<!--              <span>{{price}}</span>-->
<!--              <img src="../../public/static/images/mini-info.svg" alt="1.jpg">-->
<!--              <img src="../../public/static/images/mini-edit.svg" alt="1.jpg">-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="giftItemDelete">-->
<!--            <img src="../../public/static/images/mini-delete.svg" alt="1.jpg">-->
<!--          </div>-->
<!--        </div>-->
        <div v-for="gift in gifts" v-bind:key="gift.id" class="giftItemInGroup d-flex">
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
<!--        <div class="giftItemInGroup d-flex">-->
<!--          <div class="giftItemInfo">-->
<!--            <div class="giftItemImg"><img src="../../public/static/images/big_clock.svg" alt="1.jpg"></div>-->
<!--            <div class="giftItemName text-left">{{name}}</div>-->
<!--            <div class="giftItemPrice text-left d-flex p-0 justify-content-between">-->
<!--              <span>{{price}}</span>-->
<!--              <img src="../../public/static/images/mini-info.svg" alt="1.jpg">-->
<!--              <img src="../../public/static/images/mini-edit.svg" alt="1.jpg">-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="giftItemDelete">-->
<!--            <img src="../../public/static/images/mini-delete.svg" alt="1.jpg">-->
<!--          </div>-->
<!--        </div>-->
      </div>
      <div class="col-1 d-flex justify-content-center align-items-center">
        <img src="../../public/static/images/to-right.svg" alt="1.jpg">
      </div>
      <div class="col-1"></div>
    </div>
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

  export default {
    name: "Profile_GIFT",
    data () {
      return {
        // "user": 1,
        // "name": "string",
        // "description": "string",
        // "photo": null,
        // "link": null,
        // "price": 50
        'gifts': {}
      }
    },
    methods: {
      getGifts() {
        Gifts.read().then(response => {
          this.gifts = response
        })
      }
    },
    beforeMount() {
      this.getGifts()
    }
  }
</script>

<style scoped>

</style>