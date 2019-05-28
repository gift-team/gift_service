<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  // mounted(){
  //   let styles = document.createElement('link')
  //   styles.setAttribute('rel', 'stylesheet')
  //   styles.setAttribute('href', 'static/style.css')
  //   document.head.appendChild(styles)
  //   styles = document.createElement('link')
  //   styles.setAttribute('rel', 'stylesheet')
  //   styles.setAttribute('href', 'static/bootstrap4/css/bootstrap.min.css')
  //   document.head.appendChild(styles)
  //   styles = document.createElement('link')
  //   styles.setAttribute('rel', 'stylesheet')
  //   styles.setAttribute('href', 'https://fonts.googleapis.com/css?family=Montserrat')
  //   document.head.appendChild(styles)
  //   styles = document.createElement('link')
  //   styles.setAttribute('rel', 'stylesheet')
  //   styles.setAttribute('href', 'https://use.fontawesome.com/releases/v5.8.1/css/all.css')
  //   document.head.appendChild(styles)
  //   let script = document.createElement('script')
  //   script.setAttribute('src', 'https://code.jquery.com/jquery-3.3.1.slim.min.js')
  //   document.head.appendChild(script)
  //   script = document.createElement('script')
  //   script.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js')
  //   document.head.appendChild(script)
  //   script = document.createElement('script')
  //   script.setAttribute('src', 'static/bootstrap4/js/bootstrap.min.js')
  //   document.head.appendChild(script)
  // }
}
</script>

<style>
@font-face {
    font-family: "MontEB";
    src: url("fonts/Montserrat-ExtraBold.ttf");
}

@font-face {
    font-family: "MontB";
    src: url("fonts/Montserrat-Bold.ttf");
}

.container{
    max-width: 1440px;
    padding: 0;
    margin: auto;
}

.title{
    margin: auto;
    width: 100%;
}

.titleMenu{
    width: 100%;
}

.bgNav{
    background: #7F2BC1;
}

.navbar-toggler{
    background: white;
}

.navGroup .nav-link{
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 20px;
    line-height: normal;
    color: white;
}

/*.logoTitle img{*/
/*width: 380px;*/
/*height: 110px;*/
/*margin: auto;*/
/*}*/

.logoTitle{
    margin-top: 54px;
}

.regBtnTitle{
    height: 40px;
    width: 190px;
    background: #7F2BC1;
    border-radius: 10px;
    font-family: Montserrat, sans-serif;
    letter-spacing: 0.5px;
    font-style: normal;
    font-weight: bold;
    font-size: 14px;
    line-height: normal;
    color: #FFFFFF;
    outline: none!important;
}

.menu{
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 14px;
    line-height: normal;
    color: #7F2BC1;
    margin-top: 34px;
    /*padding-bottom: 20px;*/
    padding-left: 40px!important;
}

.menu a {
    text-decoration: none!important;
    color: #7F2BC1;
}

.mainLeft{
    margin-top: 113px;
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: normal;
    /*font-size: 72px;*/
    line-height: normal;
    color: #535452;
}

.mainLeft h1{
    margin: 0;
    font-family: MontEB, sans-serif;
    font-style: normal;
    font-weight: 800;
    font-size: 48px;
    line-height: normal;
    color: #535452;
}

.mainLeft span{
    padding-bottom: 20px;
    font-size: 36px;
    font-weight: normal;
    font-family: Montserrat, sans-serif;
}

/*.giftBtn{*/
/*height: 40px;*/
/*margin-top: 20px;*/
/*background: #7F2BC1;*/
/*border-radius: 20px;*/
/*font-family: MontB, sans-serif;*/
/*font-style: normal;*/
/*font-weight: bold;*/
/*font-size: 14px;*/
/*line-height: normal;*/
/*color: #FFFFFF;*/
/*outline: none!important;*/
/*}*/

/*.mainRight{*/
/*max-width: 564.71px!important;*/
/*max-height: 564.71px!important;*/
/*}*/

.mainRight img{
    margin-top: 55px;
}

.ourServices{
    margin-top: 238px;
    margin-bottom: 277px;
}

.servicesHeader{
    font-family: MontB, sans-serif;
    margin-bottom: 139px;
    font-style: normal;
    font-weight: bold;
    font-size: 36px;
    line-height: normal;
    color: #535452;
}

/*.servicesItems img{*/
/*max-height: 400px;*/
/*}*/

.serviceItem{
    position: relative;
}

.servicesText{
    position: absolute;
    top: 70%;
    left: 0;
    width: 100%;
    padding: 0 17%;

}

.servicesText h3{
    font-family: Montserrat, sans-serif;
    font-style: normal!important;
    font-weight: 600;
    font-size: 18px;
    line-height: 0!important;
    color: #FFFFFF;
}

.servicesText span{
    margin-top: 10px;
    font-family: Montserrat, sans-serif;
    font-style: normal!important;
    font-weight: 300;
    line-height: normal;
    font-size: 14px;
    text-align: center;
    color: #FFFFFF;
}

/*@media (max-width: 980px) {*/
/*.servicesText span{*/
/*font-size: 13px;*/
/*}*/
/*.servicesText h3{*/
/*font-size: 20px;*/
/*}*/
/*}*/

.leftItem{
    background: url("images/LIST.svg"), no-repeat;
    background-size: contain;
    margin: auto;
    /*min-height: 300px;*/
    /*min-width: 360px;*/
    /*max-width: 215px;*/
}

.middleItem{
    background: url("images/CART.svg"), no-repeat;
    background-size: contain;
    margin: auto;
    /*min-height: 300px;*/
    /*min-width: 360px;*/
    /*max-width: 215px;*/
}

.rightItem{
    background: url("images/FRIENDS.svg"), no-repeat;
    background-size: contain;
    margin: auto;
    /*min-height: 300px;*/
    /*min-width: 360px;*/
    /*max-width: 215px;*/
}

.aboutUs{
    background: url("images/aboutBG.png"), no-repeat;
    background-size: cover;
    min-height: 846px;
    /*max-width: 100%;*/
    margin: 0;
    padding-top: 49px;
    /*padding-bottom: 50px;*/
    /*padding-left: 30px;*/
    /*padding-right: 30px;*/
}

.aboutUsHeader{
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 36px;
    line-height: normal;
    color: #535452;
    /*max-height: 100px;*/
}

.aboutLeft{
    min-height: 753px;
}

.aboutLeft h3, .aboutRight h3{
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: normal;
    color: #535452;
}

.aboutLeft span, .aboutRight span{
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 300;
    font-size: 18px;
    line-height: normal;
    color: #535452;
}

.leftText{
    padding-left: 20px!important;
}

.aboutUs img{
    width: 100%;
}

.registration{
    margin: auto;
    padding-top: 50px;
    padding-bottom: 263px;
    background: #FFFFFF;
}

.authentication{
    padding-bottom: 189px!important;
}

.regHeader{
    max-width: 100%;
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    color: #535452;
}

.regForm input{
    margin: 20px 0;
    height: 50px;
    background: #FFFDFD;
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;
    outline: none;
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;
    color: #535452;

}

.regForm form{
    padding: 0 12px!important;
}


.check span{
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;
    text-align: center;
    color: #535452;
}

.regForm label{
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 800;
    font-size: 14px;
    text-align: center;
    color: #535452;
    margin-bottom: 20px;
}

.regForm input::placeholder{
    color: #535452;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 800;
    font-size: medium;
    line-height: normal;
}

.regBtn{
    height: 60px;
    background: #7F2BC1;
    border-radius: 20px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 3.5vw;
    line-height: normal;
    color: #FFFFFF;
    outline: none!important;
}

.lendBts img{
    width: 100%;
}

/*@media (min-width: 768px) {*/
/*.regBtn{*/
/*font-size: 2vw!important;*/
/*}*/
/*.regBtnTitle{*/
/*font-size: 1.5vw!important;*/
/*}*/
/*.giftBtn{*/
/*font-size: 1.5vw!important;*/
/*}*/
/*}*/

/*@media (max-width: 576px) {*/
/*.giftBtn{*/
/*height: 40px;*/
/*padding: 0;*/
/*}*/
/*}*/

/*@media (max-width: 992px) {*/
/*.menu{*/
/*padding: 0!important;*/
/*}*/
/*.regForm input{*/
/*height: 40px!important;*/
/*}*/
/*.regBtn{*/
/*height: 40px!important;*/
/*font-size: 2.5vw!important;*/
/*}*/
/*.regBtnTitle{*/
/*height: 40px!important;*/
/*font-size: 2.5vw!important;*/
/*}*/
/*.giftBtn{*/
/*max-height: 40px!important;*/
/*font-size: 2.5vw!important;*/
/*}*/
/*}*/

/*.imgFooter{*/
/*position: relative;*/
/*top: 83px;*/
/*left: 120px;*/
/*}*/

.footer{
    /*position: relative;*/
    /*min-height: 277px;*/
    /*padding: 0 20px;*/

    background: rgba(151, 77, 208, 0.65);
    /*clear: both;*/
}

.footerMenu{
    margin-top: 36px;
    padding: 0;
}

.imgFooter{
    min-height: 132px;
    min-width: 413px;
}

.footerMenu p{
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: normal;
    color: #FFFFFF;
}

.footerBottom img{
    padding-left: 7px;
    padding-top: 17px;
}

/*.footerBottom{*/
/*clear: both;*/
/*}*/

/*@media (max-width: 768px) {*/
/*.footerMenu p{*/
/*font-size: 15px;*/
/*margin: 10px!important;*/
/*}*/
/*.copyright{*/
/*font-size: 15px!important;*/
/*padding: 10px!important;*/
/*}*/
/*.social i{*/
/*padding-top: 10px!important;*/
/*}*/
/*}*/

.left{
    position: relative;
    margin-top: 36px;
}

.copyright{
    /*padding-top: 105px;*/
    /*padding-left: 20px;*/
    /*padding-bottom: 20px;*/
    position: absolute;
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: normal;
    color: #FFFFFF;
    z-index: 100;
    bottom: 17px;
}

.social img{
    font-size: 60px;
    color: #FFFFFF;
    /*padding-left: 31px;*/
    /*padding-right: 31px;*/
    /*padding-top: 90px;*/
}

/*@media (min-width: 768px) {*/
/*.footer{*/
/*padding-left: 40px!important;*/
/*padding-right: 80px!important;*/
/*}*/
/*}*/

.giftCreationForm{
    width: 780px!important;
    height: 720px;
}

.giftCreationHeader{
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 48px;
    line-height: 59px;/* identical to box height */
    padding-top: 36px;
    padding-bottom: 50px;
    color: #535452;
}

.giftCreationInfo{
    min-height: 100px;

}

.giftCard{
    background: #7F2BC1;
    border-radius: 20px;
    padding: 24px 26px 8.7px;
    min-height: 214.68px;
}

.giftInfoPrice{
    margin-top: 17.32px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 800;
    font-size: 18px;
    line-height: 22px;
    color: #535452;
}

.giftInfoPrice input{
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;
    height: 50px;
    border: none;
}

.giftInfoPrice input::placeholder{
    padding-left: 15px;
    font-family: Montserrat, sans-serif;
    font-weight: 800;
}

.giftCreationInfo button{
    margin-top: 122px;
    height: 50px;
    background: #7F2BC1;
    border-radius: 10px;
    font-family: MontB, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 18px;
    line-height: normal;
    color: #FFFFFF;
    outline: none!important;
}

.giftCreationUrl{
    margin-top: 41px;
}

.giftCreationDesc{
    margin-top: 29px;
    height: 179px!important;
}


.giftInfoPrice textarea{
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;
    height: 50px;
    resize: none;
    border: none;

}

.giftInfoPrice textarea::placeholder{
    padding-left: 22px;
    padding-top: 19px;
    font-family: Montserrat, sans-serif;
    font-weight: 800;
}

.giftCreationName::placeholder{
    padding-left: 22px!important;
}

.giftCreationUrl::placeholder{
    padding-left: 22px!important;
}

.giftCreationCollection{
    margin-top: 27px;
    text-align: left;
}

.collectionHeader{
    margin-left: 21.5px;
}

.collectionImages{
    margin-top: 13px;
}

.collectionImages div{
    width: 43px;
    height: 43px;
    border-radius: 10px;
}

.collectionImages div:nth-child(1){
    background: rgba(101, 187, 94, 1);
}

.collectionImages div:nth-child(2){
    background: #DC4E41;
}

.collectionImages div:nth-child(3){
    background: rgba(83, 84, 82, 1);
}

.collectionImages div:nth-child(4){
    background: rgba(90, 102, 209, 1);
}

.collectionImages div:nth-child(5){
    background: rgba(127, 43, 193, 1);
}

button {
    border: none;
}

textarea:focus, input:focus{
    outline: none;
}

.userItem {
    position: relative;
    width: 1100px;
    margin-left: 170px;
}

.userItemData {
    /*margin-top: 79px;*/
}

.userItemImg {
    position: relative;
    background: url("images/MeganFox.jpg") #FFFFFF center center;
    background-size: cover;
    border: 3px solid #7F2BC1;
    box-sizing: border-box;
    box-shadow: 0px 8px 4px rgba(0, 0, 0, 0.25);
    width: 258.67px;
    height: 258.67px;
    border-radius: 50%;
    /*left: 105px;*/

}


.userItemName {
    width: 217.72px;
    height: 250.77px;
    background: #7F2BC1;
    border-radius: 20px;
    margin-top: -86px;




}

.userItemNameText {
    position: relative;
    top: 108px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: normal;
    text-align: center;
    color: #FFFFFF;
}

.userItemNameTextEdit{
    position: relative;
    margin-top: 120px;
}


.userDataName {
    display: block;
    /*height: 153px;*/
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 48px;
    line-height: normal;
    margin-left: 0;

    color: #535452;
}

.userDataWish {
    /*display: inline-block;*/
    padding-top: 20px;
    width: 230px;
    height: 270px;
    background: #7F2BC1;
    border-radius: 20px;
}

.userDataWishImg {
    position: relative;
    width: 177px;
    height: 177px;
    margin-left: 26px;

    background: url("images/apple_watch.png") #FFFFFF center center;
    background-size: cover;
    box-shadow: 0px 8px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.userDataWishName {
    position: relative;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: normal;

    color: #FFFFFF;

    margin-top: 12px;
}

.userDataNewWish {
    width: 230px;
    height: 270px;
    background: #F5BA3D;
    border-radius: 20px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: normal;

    color: #FFFFFF;

}

.userDataWishLook {
    width: 230px;
    height: 57px;
    margin-top: 22px;
    background: #FDA736;
    border-radius: 20px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: normal;

    color: #FFFFFF;
}

/*Friend*/

.userFriendsHeader {
    margin-left: 105px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 48px;
    line-height: normal;

    color: #535452;
}

.userFriendItem {
    position: relative;
    width: 1100px;
    margin-left: 170px;
}

.userFriendItemData {
    margin-top: 37px;
}

.userFriendItemImg {
    position: relative;
    background: url("images/MeganFox.jpg") #FFFFFF center center;
    background-size: cover;
    border: 3px solid #7F2BC1;
    box-sizing: border-box;
    box-shadow: 0px 8px 4px rgba(0, 0, 0, 0.25);
    width: 225px;
    height: 225px;
    border-radius: 50%;
}


.userFriendItemName {
    width: 189.38px;
    height: 218.12px;
    background: #7F2BC1;
    border-radius: 20px;
    margin-top: -86px;
    margin-left: 18px;
}



.userFriendItemNameText {
    position: relative;
    top: 108px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: normal;
    text-align: center;
    color: #FFFFFF;
}

/*Wish*/

.myWishesTitle {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: normal;

    color: #535452;
    left: 108px;
}


.myWishesNameLogo {
    width: 40px;
    height: 40px;
    margin-right: 11px;
    background: #535452;
    border-radius: 10px;
}

.myWishesNameLogo img {
    margin-bottom: 7px;
    margin-left: 5px;
}

.myWishesNameText {
    position: relative;
    float: left;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: normal;
    margin-left: 20px;

    color: #535452;

}

.myWishesData {
    margin-top: 25px;
}

.myWishesFilter {
    padding-left: 139px;
}



.myWishesFilterTitle {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: normal;

    color: #535452;
}

.myWishesFilterName {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;

    color: #535452;
}

.myWishFilterRow {
    margin-top: 20px;
}
.myWishesDropdown {
    width: 174px;
    height: 30px;

    background: #FFFDFD;
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: normal;

    color: #535452;
}

.myWishesCreate {
    margin-top: 99px;
}

.myWishesCreateText {
    font-family: Montserrat,sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: normal;

    color: #535452;
}

.myWishesCreateButton {
    width: 230px;
    height: 57px;
    background: #FDA736;
    border-radius: 20px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: normal;

    color: #FFFFFF;
}

.myWishesEl {
    height: 580px;
}

.myWishesElArr {
}

.myWishesElData {
    float: left;
    width: 269px;
    height: 101px;
    margin: 20px;
}

.myWishesElText {
    width: 269px;
    height: 52px;

    background: #7F2BC1;
    border-radius: 10px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 18px;
    line-height: normal;
    padding-left: 120px;
    padding-top: 5px;

    color: #FFFFFF;
}

.myWishesElTextDate {
    font-weight: normal;
    font-size: 16px;
}
.myWishesElImg {
    float: left;
    width: 100px;
    height: 100px;
    margin-top: -53px;

    background: url("images/apple_watch.png") #FFFFFF center center;
    background-size: cover;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;
}

.myWishesElInfo {
    float: left;
    width: 40px;
    height: 40px;
    margin-top: 7px;
    margin-left: 16px;
    padding-left: 10px;

    background: #F5BA3D;
    border-radius: 10px;
}

.myWishesElInfo img {
    margin-top: 9px;
}

.myWishesElDel {
    float: left;
    width: 40px;
    height: 40px;
    margin-top: 7px;
    margin-left: 16px;
    padding-left: 10px;

    background: #DC4E41;
    border-radius: 10px;
}

.myWishesElDel img {
    margin-top: 9px;
}


/*Edit*/

.userEditItemData {
    margin-top: 79px;
}

.userEditData {
    margin-top: 90px;
}

.userEditDataProfile {
    width: 259px;
}

.userEditItemImg {
    position: relative;
    background: url("images/profile.svg") #FFFFFF center center;
    background-size: cover;
    border: 3px solid #7F2BC1;
    box-sizing: border-box;
    box-shadow: 0px 8px 4px rgba(0, 0, 0, 0.25);
    width: 258.67px;
    height: 258.67px;
    border-radius: 50%;

}


.userEditItemName {
    width: 217.72px;
    height: 250.77px;
    background: #7F2BC1;
    border-radius: 20px;
    margin-top: -86px;

    margin-left: 20px;


}

.userEditItemNameText {
    position: relative;
    top: 108px;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: normal;
    text-align: center;
    color: #FFFFFF;
}

.userEditItemNameTextCloud{
    position: relative;
    margin-top: 120px;
}

.userEditDataData {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: normal;

    color: #535452;
}

.userEditDataSecond {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: normal;
    margin-top: 90px;

    color: #535452;
}

.userEditDataThird {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 600;
    font-size: 36px;
    line-height: normal;


    color: #535452;
}

.userEditDataDataSecond img {
    position: relative;
    bottom: 10px;
    margin-left: 120px;
}

.userEditDataForm {
    width: 100%;
    height: 50px;

    background: #FFFDFD;
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    margin-top: 18px;
    margin-right: 15px;
    margin-left: 15px;


    padding-right: 15px;
    padding-left: 15px;
}

.userEditDataFormLogin {
    width: 100%;
    height: 50px;

    background: #FFFDFD;
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    margin-top: 18px;
    margin-right: 15px;

    padding-right: 15px;
    padding-left: 15px;
}

.userEditDataFormSmall {
    width: 100%;
    height: 50px;

    background: #FFFDFD;
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    margin-top: 18px;
}


.userEditDataFormDataName {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;

    color: #535452;

    margin-top: 11px;

}

.userEditDataFormData {
    width: 189px;
    height: 50px;

    background: #FFFDFD;
    box-shadow: inset 4px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 10px;

    margin-top: 11px;
    /*margin-left: -15px;*/
}

.userEditDataFormGenderName {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;

    margin-top: 11px;


    color: #535452;
}

.userEditDataFormGenderDataMale {
    float: left;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;
    margin-top: 25px;

    color: #535452;
}

.userEditDataFormGenderDataFemale {
    float: left;
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;
    margin-left: 30px;
    margin-top: 25px;

    color: #535452;
}

.userEditDataCheck {
    height: 40px;
    width: 100%;
    margin-top: 23px;
    margin-bottom: 5px;

    background: #7F2BC1;
    border-radius: 10px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 14px;
    line-height: normal;

    color: #FFFFFF;
}

.userEditDataAdd {
    height: 40px;
    width: 100%;
    margin-top: 23px;
    margin-bottom: 5px;

    background: #7F2BC1;
    border-radius: 10px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 14px;
    line-height: normal;

    color: #FFFFFF;
}

.userEditDataSave {
    height: 40px;
    width: 100%;
    margin-top: 23px;
    margin-bottom: 5px;


    background: #7F2BC1;
    border-radius: 10px;

    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: bold;
    font-size: 14px;
    line-height: normal;

    color: #FFFFFF;
}

.userEditDataDataProfType {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;
    margin-top: 34px;
    margin-bottom: 12px;

    color: #535452;
}

.userEditDataDataMent {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
    line-height: normal;
    margin-top: 30px;
    margin-left: 15px;

    color: #535452;

    position: relative;
}

.userEditDataDataMent input {
    position: relative;
    float: left;
}



.filter h2 {
    font-size: 36px;
    color: #535452;
    margin-top: 30px;
}

.filter h3 {
    font-size: 24px;
    color: #535452;
}

.myWishesH2 {
    text-align: center;
}
</style>
