<template>
  <block-ab title="Содействие трудоустройству выпускников">
    <SplitLinks :links="links" />
    <div class="block-zxc__right">
      <common-documents-list json-path="documents/assistance-links-1.json" />
      <common-documents-list json-path="documents/assistance-links-2.json" />
      <common-documents-list json-path="documents/assistance-links-3.json" />
      <common-documents-list json-path="documents/assistance-links-4.json" />
      <common-documents-list json-path="documents/assistance-links-5.json" />
      <common-documents-list json-path="documents/assistance-links-6.json" />
    </div>
    <p class="ab__p">
      Основной целью деятельности Центра карьеры является обеспечение условий для марш-рутизации и
      трудоустройства обучающихся и выпускников колледжа в соответствии с освоенной, в том числе
      инвалидов и лиц с ОВЗ.
    </p>
    <p class="ab__p">Направления работы Центра карьеры:</p>
    <ul class="ab__list">
      <li>
        взаимодействие с государственными учреждениями службы занятости по вопросам трудоустройства
        выпускников колледжа;
      </li>
      <li>обеспечение индивидуализации профессионального развития выпускников;</li>
      <li>
        создание, ведение и актуализация банка вакансий для постоянной и временной занятости
        обучающихся и выпускников посредством портала Re-works (<a
          target="_blank"
          href="https://re-works.ru/"
          >https://re-works.ru/</a
        >) и официальной группы ВКонтакте «Центр карьеры БПОУ «КИТЭК» (<a
          target="_blank"
          href="https://vk.com/trudkitek"
          >https://vk.com/trudkitek</a
        >);
      </li>
      <li>
        создание и ведение базы резюме обучающихся и выпускников (с их согласия) посредством портала
        Re-works (<a target="_blank" href="https://re-works.ru/">https://re-works.ru/</a>);
      </li>
      <li>
        подбор вакансий по заявкам выпускников и подбор соискателей по заявкам работодателей, в том
        числе по образовательным программам ФП «Профессионалитет»;
      </li>
      <li>
        организация и участие в мероприятиях по вопросам трудоустройства (ярмарки вакансий, дней
        карьеры, встреч с работодателями и т.п.) с работодателями образовательного кластера среднего
        профессионального образования «Союз+» в отрасли «Туризм и сфера услуг» (в рамках ФП
        «Профессионалитет»);
      </li>
      <li>
        сопровождение заключения соглашений с работодателями в целях маршрутизации и трудоустройства
        обучающихся и выпускников, в том числе по образовательным программам ФП «Профессионалитет»;
      </li>
      <li>
        проведение семинаров и тренингов, направленных на подготовку обучающихся и выпускников к
        поиску работы и трудоустройству.
      </li>
    </ul>
    <p class="ab__p"><b>Координатор по трудоустройству:</b> Савельева Юлия Сергеевна</p>
    <p class="ab__p"><b>Телефон Центра карьеры:</b> 8 (3812) 68-13-68</p>
    <p class="ab__p">
      <a
        href="https://2gis.ru/omsk/firm/282003257722518?m=73.38383%2C55.026562%2F16"
        target="_blank">
        <b>Адрес:</b> 644069 г. Омск, ул. 24-я Северная, 1236.
      </a>
    </p>
    <p class="ab__p"><b>E-mail:</b> tradeconomy@mail.ru</p>

    <div class="block-zxc__bottom">
      <common-documents-list json-path="documents/assistance-links-1.json" />
      <common-documents-list json-path="documents/assistance-links-2.json" />
      <common-documents-list json-path="documents/assistance-links-3.json" />
      <common-documents-list json-path="documents/assistance-links-4.json" />
      <common-documents-list json-path="documents/assistance-links-5.json" />
      <common-documents-list json-path="documents/assistance-links-6.json" />
    </div>

    <p class="ab__p"><b>Полезные ссылки:</b></p>
    <swiper :options="opts">
      <swiper-slide class="ab__slide" v-for="(i, ii) of sites" :key="ii">
        <a target="_blank" :href="i">
          <img class="ab__img" :src="`/img/assistance/${ii}.png`" />
        </a>
      </swiper-slide>
    </swiper>
    <!-- <h2 class="ab__subtitle">Новости:</h2>
    <div class="news">
      <EntitiesNewCard
        v-for="(n, nIdx) of news"
        :key="nIdx"
        :instance="n"
        v-if="n.teg == 'ticket'" />
    </div> -->
    <!-- Блок Карьерные карты -->
    <div class="h2-container">
      <h2 class="h2-zagolovok">Карьерные карты</h2>
    </div>
    <p class="ab__p ab__p--pointer" @click="showCareer = !showCareer">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
      <b> Показать/скрыть карьерные карты</b>
    </p>
    <block-ab v-show="showCareer" class="imgblock">
      <div class="img-container">
        <img
          v-for="n in 7"
          :key="'career-' + n"
          class="img-single__minimg"
          :src="`/img/career-cards/${n}.webp`"
          @click="openImg(`/img/career-cards/${n}.webp`)"
          alt="Карьерная карта" />
      </div>
    </block-ab>

    <!-- Блок Самозанятые -->
    <div class="h2-container">
      <h2 class="h2-zagolovok">Как стать самозанятым</h2>
    </div>
    <p class="ab__p ab__p--pointer" @click="showSamo = !showSamo">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
      <b> Показать/скрыть самозанятых</b>
    </p>
    <block-ab v-show="showSamo" class="imgblock">
      <div class="img-container">
        <img
          v-for="n in 6"
          :key="'samo-' + n"
          class="img-single__minimg"
          :src="`/img/samo-z/${n}.webp`"
          @click="openImg(`/img/samo-z/${n}.webp`)"
          alt="Самозанятые" />
        <br />
        <div class="conte">
          <p class="ab__p">
            <a href="https://www.gosuslugi.ru/help/news/2019_08_30_registraciya_samozanyatyh"
              >Регистрация самозанятых</a
            >
          </p>
        </div>
      </div>
    </block-ab>

    <!-- Блок Самозанятые -->
    <div class="h2-container">
      <h2 class="h2-zagolovok">
        Работа и практика на предприятиях оборонно-промышленного комплекса для студентов на
        платформе ФКЦ ОПК
      </h2>
    </div>
    <p class="ab__p ab__p--pointer" @click="opk = !opk">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
      <b> Показать/скрыть ОПК</b>
    </p>
    <block-ab v-show="opk" class="">
      <div class="opk-employment-info">
        <h2>Трудоустройство студентов и выпускников в ОПК</h2>

        <div class="portal-info">
          <h3>Федеральный кадровый центр ОПК</h3>
          <p>
            Студенты и выпускники колледжа могут разместить свое резюме и посмотреть вакансии
            предприятий ОПК на портале
            <a href="https://fkc-opk.ru" target="_blank" rel="noopener noreferrer"
              >Федерального кадрового центра оборонно-промышленного комплекса</a
            >
            (ФКЦ ОПК) в информационном сервисе:
          </p>
          <blockquote>
            <strong
              >«Трудоустройство студентов в организации оборонно-промышленного комплекса»</strong
            >
          </blockquote>
        </div>

        <div class="features">
          <h4>Возможности сервиса:</h4>
          <ul>
            <li>Размещение резюме на портале</li>
            <li>Адресное доведение резюме до организаций ОПК через личные кабинеты</li>
            <li>Поиск баз практики и трудоустройства в любом регионе</li>
          </ul>
        </div>

        <div class="vacancy-search">
          <h3>Поиск вакансий для практики и трудоустройства</h3>
          <p>
            Поиск вакансий предприятий ОПК можно осуществлять в разделе
            <a href="https://fkc-opk.ru/trudoustro..." target="_blank" rel="noopener noreferrer"
              >«Трудоустройство» → «Вакансии организаций предприятий ОПК»</a
            >
            (доступно без регистрации).
          </p>
        </div>

        <div class="registration">
          <h3>Регистрация студентов колледжа на портале ФКЦ ОПК</h3>
          <p>Регистрация реализована в формате общего доступа от БПОУ «КИТЭК» по единому паролю:</p>
          <div class="credentials">
            <p><strong>Логин:</strong> Student_KITEK</p>
            <p><strong>Пароль:</strong> Student1!</p>
          </div>
          <p>Для входа на портал:</p>
          <ol>
            <li>
              Перейдите на
              <a href="https://fkc-opk.ru" target="_blank" rel="noopener noreferrer">fkc-opk.ru</a>
            </li>
            <li>В блоке «Вход для представителей организаций» выберите пункт «Для студентов»</li>
            <li>Введите предоставленные логин и пароль</li>
          </ol>
          <p>
            Прямая ссылка для входа:
            <a href="https://fkc-opk.ru/Account/Lo..." target="_blank" rel="noopener noreferrer"
              >fkc-opk.ru/Account/Lo...</a
            >
          </p>
        </div>

        <div class="personal-auth">
          <h3>Персональная авторизация</h3>
          <p>
            После входа по общему паролю необходимо пройти персональную авторизацию, установив свой
            индивидуальный пароль.
          </p>
        </div>

        <div class="resume-creation">
          <h3>Создание резюме</h3>
          <p>
            Инструкция по созданию резюме представлена в Приложении №1. Резюме создается для
            следующих типов вакансий:
          </p>
          <ul>
            <li>Производственная практика</li>
            <li>Стажировка</li>
            <li>Трудоустройство</li>
          </ul>
        </div>

        <div class="additional-resources">
          <h3>Дополнительные ресурсы</h3>
          <p>
            Студенты и выпускники могут просматривать еженедельное обновление вакансий ОПК на
            интерактивном портале:
          </p>
          <p>
            <a
              href="https://omskzan.ru/content/вакансии_оборонно_промышленного_комплекса"
              target="_blank"
              rel="noopener noreferrer"
              >«Работа России» - служба занятости Омской области</a
            >
          </p>
        </div>
      </div>
    </block-ab>

    <div class="h2-container">
      <h2 class="h2-zagolovok">Как стать индивидуальным предпринимателем</h2>
    </div>
    <p class="ab__p ab__p--pointer">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
      <b>
        <a href="https://www.sberbank.com/ru/s_m_business/pro_business/kak-otkryt-ip"
          >Перейти на сайт</a
        ></b
      >
    </p>

    <!-- Lightbox для полноэкранного просмотра картинки -->
    <div v-if="showImg" class="lightbox" @click="showImg = false">
      <img :src="imgSrc" class="lightbox__img" />
      <span class="lightbox__close" @click.stop="showImg = false">&times;</span>
    </div>

    <div class="h2-container">
      <h2 class="h2-zagolovok">Видео</h2>
    </div>
    <p class="ab__p ab__p--pointer" @click="showSpo = !showSpo">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper>
      <b> Показать/скрыть видео</b>
    </p>
    <block-ab v-show="showSpo" class="imgblock">
      <div class="">
        <div class="video-wrapper">
          <div class="video-container">
            <video class="ab__video" controls playsinline>
              <source src="/video/prepodtryd.mp4" type="video/mp4" />
              Ваш браузер не поддерживает видео
            </video>
          </div>

          <div class="video-caption">
            <p class="ab__p">
              <b>Савельева Ю.С.</b>, руководитель отдела содействия трудоустройству и взаимодействия
              с работодателями
            </p>
          </div>
        </div>
      </div>
    </block-ab>

    <!-- 
    <p class="ab__p" @click=";(kk = !kk), (visible = false)">
      <icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
      ><b>  NAME</b>
    </p>
    <div v-show="kk">
      <block-ab title="title">

        <p class="ab__p click ab__link">
          <b red-prim
            ><icon-wrapper class="icon-tap" width="20" height="24"><icon-tapclick /></icon-wrapper
            ><a href="https://www.omsktec.ru/student/sportclub"
              >Студенческий спортивный клуб "Старт"</a
            ></b
          >
        </p>
      </block-ab>
    </div> -->
  </block-ab>
</template>

<script>
import { loadDynamic } from '~/core/helpers/file'
export default {
  async created() {
    this.assistanceDocuments = await loadDynamic('documents/assistance-page.html')
  },

  data() {
    return {
      showCareer: false,
      showSpo: false,
      showSamo: false,
      opk: false,
      showImg: false,
      imgSrc: '',
      assistanceDocuments: 'Загрузка...',
      sites: [
        'https://re-works.ru/?ysclid=mayv69q66y526098368/',
        'https://vk.com/trudkitek',
        'https://jobkadrov.ru/',
        'https://www.omskzan.ru/',
        'https://omsk.hh.ru/',
        'https://omsk.superjob.ru/',
        'https://omsk.zarplata.ru/',
        'https://мойбизнес-55.рф/',
        'https://fkc-opk.ru/',
        'https://skillsnet.ru/',
        'https://gossluzhba.gov.ru/',
      ],
      opts: {
        slidesPerView: 4,
        autoplay: {
          enabled: true,
          delay: 3000,
        },
      },
    }
  },
  methods: {
    openImg(src) {
      this.imgSrc = src
      this.showImg = true
    },
  },
}
</script>

<style scoped lang="scss">
// стили видео
.video-wrapper {
  max-width: 800px;

  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.video-wrapper:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.video-container {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* Соотношение сторон 16:9 */
  background: #000;
}

.ab__video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
  outline: none;
}

.video-caption {
  padding: 20px;
  text-align: center;
  border-top: 1px solid #eee;
}

.ab__p {
  font-size: 18px;
  margin-bottom: 0;
  color: #2c3e50;
}

.ab__p b {
  color: #3498db;
  font-weight: 600;
}

/* Стили для элементов управления видео */
.ab__video::-webkit-media-controls-panel {
  background: rgba(0, 0, 0, 0.7);
}

.ab__video::-webkit-media-controls-play-button,
.ab__video::-webkit-media-controls-volume-slider,
.ab__video::-webkit-media-controls-timeline {
  filter: invert(1); /* Делаем элементы управления белыми */
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .video-wrapper {
    border-radius: 8px;
  }

  .video-caption {
    padding: 15px;
  }

  .ab__p {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  body {
    padding: 10px;
  }

  .ab__p {
    font-size: 15px;
  }
}
// конец стилей видео
.opk-employment-info {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  max-width: 900px;

  padding: 20px;
}

.opk-employment-info h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
}

.opk-employment-info h3 {
  color: #2980b9;
  margin-top: 25px;
}

.opk-employment-info h4 {
  color: #16a085;
}

.credentials {
  background: #f8f9fa;
  padding: 10px 15px;
  border-left: 4px solid #3498db;
  margin: 10px 0;
}

blockquote {
  background: #f9f9f9;
  border-left: 5px solid #ccc;
  margin: 1.5em 10px;
  padding: 0.5em 10px;
  font-style: italic;
}

a {
  color: #2980b9;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

ul,
ol {
  padding-left: 20px;
}

li {
  margin-bottom: 5px;
}

.ab {
  &__sites {
    position: absolute;
    right: 24px;
    top: 24px;
    display: block;
  }
  &__img {
    width: 200px;
    height: 150px;
    object-fit: contain;
    margin-top: 24px;
  }
  &__slide {
  }
}

// <div class="h2-container">
//       <h2 class="h2-zagolovok">Карьерные карты</h2>
//     </div>

.h2-container {
  margin-left: 1rem;
  margin-top: 2rem;
}
.h2-zagolovok {
  font-size: 1.2rem;
  font-weight: bold;
  color: #c43e3e;
}
.helper {
  position: relative;
  margin: 0;
  text-align: center;
  width: 660px;
  &__li {
    position: absolute;
    display: inline-block;
    width: 30px;
    height: 30px;
  }
  .alternate li {
    -webkit-animation: shake 1s linear alternate infinite;
    animation: shake 1s linear alternate infinite;
  }
  @-webkit-keyframes shake {
    100% {
      -webkit-transform: translateX(-50px);
    }
  }
  @keyframes shake {
    100% {
      transform: translateX(-50px);
    }
  }
}
.ab__p--pointer {
  cursor: pointer;
  user-select: none;
  margin-bottom: 0.5rem;
  margin-top: 0.5rem;
}

.conte {
  display: flex;
}
.imgblock {
  background: #f7f9fa;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  padding: 1rem 1.5rem 1.5rem 1.5rem;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
}
.img-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: flex-start;
}
.img-single__minimg {
  width: 450px;
  height: 350px;
  object-fit: cover;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
  transition: transform 0.2s;
  &:hover {
    transform: scale(1.07);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18);
  }
}
.lightbox {
  position: fixed;
  inset: 0;
  background: rgba(20, 20, 20, 0.93);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.lightbox__img {
  max-width: 90vw;
  max-height: 90vh;
  border-radius: 16px;
  box-shadow: 0 6px 32px rgba(0, 0, 0, 0.35);
}
.lightbox__close {
  position: fixed;
  top: 32px;
  right: 48px;
  font-size: 3rem;
  color: #fff;
  cursor: pointer;
  user-select: none;
  z-index: 10000;
  transition: color 0.2s;
  &:hover {
    color: #e74c3c;
  }
}
</style>
