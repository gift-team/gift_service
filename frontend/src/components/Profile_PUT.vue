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
                    <router-link to="/auth/register/">
                        <button class="regBtnTitle ">РЕГИСТРАЦИЯ</button>
                    </router-link>
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
                    <div class="row">
                        <input v-model="first_name" class="colform-control userEditDataForm" type="text"
                               placeholder="Имя">
                    </div>
                    <div class="row">
                        <input v-model="last_name" class="form-control userEditDataForm" type="text"
                               placeholder="Фамилия">
                    </div>
                    <div class="row">
                        <div class="col-xl-7">
                            <input v-model="login" class="form-control userEditDataFormLogin" type="text"
                                   placeholder="Логин">
                        </div>
                        <div class="col-xl-1"></div>
                        <div class="col-xl-4">
                            <button class="userEditDataCheck">Проверить</button>
                        </div>
                    </div>
                    <div class="row">
                        <input v-model="email" type="email" class="form-control userEditDataForm"
                               id="exampleInputEmail1"
                               aria-describedby="emailHelp"
                               placeholder="Enter email">
                    </div>
                    <div class="row">
                        <input v-model="phone" class="form-control userEditDataForm" type="tel" placeholder="Телефон">
                    </div>
                    <div class="row">
                        <div class="col-xl-6 userEditDataFormDataName text-left">
                            Дата рождения:
                        </div>
                        <div class="col-xl-6 userEditDataFormGenderName text-left">
                            Пол:
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xl-6">
                            <input v-model="birthdate" class="form-control userEditDataFormData" type="date">
                        </div>
                        <div class="col-xl-6 text-left">
                            <div class="form-check userEditDataFormGenderDataMale">
                                <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1"
                                       value="option1" checked>
                                <label class="form-check-label" for="exampleRadios1">
                                    М
                                </label>
                            </div>
                            <div class="form-check userEditDataFormGenderDataFemale">
                                <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2"
                                       value="option2">
                                <label class="form-check-label" for="exampleRadios2">
                                    Ж
                                </label>
                            </div>
                        </div>
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
                <div class="col-xl-4">
                    <div class="row">
                        <input v-model="country" class="form-control userEditDataForm" type="text" placeholder="Страна">
                    </div>
                    <div class="row">
                        <input v-model="region" class="form-control userEditDataForm" type="text" placeholder="Регион">
                    </div>
                    <div class="row">
                        <input v-model="region" class="form-control userEditDataForm" type="text" placeholder="Город">
                    </div>
                    <div class="row">
                        <div class="col-xl-5">
                            <button class="userEditDataAdd">Добавить</button>
                        </div>
                        <div class="col-xl-7"></div>
                    </div>
                </div>
                <div class="col-xl-2"></div>
                <div class="col-xl-4">
                    <div class="row"></div>
                    <div class="row">
                        <input v-model="street" class="form-control userEditDataForm" type="text" placeholder="Улица">
                    </div>
                    <div class="row">
                        <div class="col-xl-6">
                            <input v-model="building" class="form-control userEditDataFormSmall" type="text"
                                   placeholder="Дом">
                        </div>
                        <div class="col-xl-6">
                            <input class="form-control userEditDataFormSmall" type="text" placeholder="Корпус">
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xl-6">
                            <input v-model="flat" class="form-control userEditDataFormSmall" type="text"
                                   placeholder="Квартира">
                        </div>
                        <div class="col-xl-6">
                            <input class="form-control userEditDataFormSmall" type="text" placeholder="Индекс">
                        </div>
                    </div>
                </div>
                <div class="col-xl-1"></div>
            </div>
            <div class="row userEditDataSecond">
                <div class="col-xl-1"></div>
                <div class="col-xl-4 userEditDataData">
                    Приватность:
                </div>
                <div class="col-xl-2"></div>
                <div class="col-xl-4 userEditDataData">
                    Смена пароля:
                </div>
                <div class="col-xl-1"></div>
            </div>
            <div class="row userEditDataForth">
                <div class="col-xl-1"></div>
                <div class="col-xl-4">
                    <div class="row userEditDataDataProfType">
                        Тип профиля
                    </div>
                    <div class="row">
                        <input class="form-control userEditDataForm" type="text" placeholder="Открытый">
                    </div>
                    <div class="row form-check form-check-inline userEditDataDataMent text-left">
                        <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
                        <label class="form-check-label" for="inlineCheckbox1">Уведомления и оповещения</label>
                    </div>
                    <div class="row">
                        <div class="col-xl-6 ">
                            <button v-on:click="submitForm" class="userEditDataSave">Сохранить</button>
                        </div>
                        <div class="col-xl-6"></div>
                    </div>
                </div>
                <div class="col-xl-2"></div>
                <div class="col-xl-4">

                    <div class="row ">
                        <input type="password" class="form-control userEditDataForm" id="exampleInputPassword1"
                               placeholder="Старый пароль">
                    </div>
                    <div class="row ">
                        <input type="password" class="form-control userEditDataForm" id="exampleInputPassword1"
                               placeholder="Новый пароль">
                    </div>
                    <div class="row  ">
                        <input type="password" class="form-control userEditDataForm" id="exampleInputPassword1"
                               placeholder="Подтверждение пароля">
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
        name: "Profile_PUT",
        data() {
            return {
                "id": Number,
                "first_name": '',
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
                "flat": 0
            }
        },
        methods: {
            submitForm() {
                this.profilePut();
                return this.$router.push({name: 'profile_get'})
            },
            profilePut() {
                Profile.put({
                    "id": this.id,
                    "first_name": this.first_name,
                    "last_name": this.last_name,
                    "birthdate": this.birthdate,
                    "gender": this.gender,
                    "phone": this.phone,
                    "login": this.login,
                    "email": this.email,
                    "country": this.country,
                    "region": this.region,
                    "city": this.city,
                    "street": this.street,
                    "building": this.building,
                    "flat": this.flat
                }).catch(e => console.log(e))
            },
            getCookie(name) {
                let a = document.cookie.split('; ');
                for (let c in a) {
                    let tmp = a[c].split('=');
                    if (name === tmp[0]) {
                        return (Number(tmp[1]));
                    }
                }
            }
        },
        beforeMount() {
            this.id = this.getCookie('userId');
            this.profilePut()
        }

    }
</script>

<style scoped>

</style>