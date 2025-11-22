<template>
  <div class="events">
    <div>
      <AppBlock
        :content-style="{
          padding: '24px',
          display: 'flex',
        }"
        class="events__self"
        title="День открытых дверей ">
        <div class="opendoors">
          <div class="events__text">
            <h2 class="ab__subtitle doors">
              <!-- <b>
                Приглашаем учащихся 8-11 классов, их родителей (законных представителей),
                преподователей общеобразовательных организаций на
              </b> -->
              <!-- <b red>"Единый день открытых дверей" </b> -->

              <b red
                >Приглашаем вас на<br />
                «Единый День открытых дверей»</b
              >

              <!-- <b red>который состоится по адресу: </b>
              <b red>ул. 27-я Северная, 69</b>
              <b red>12 АПРЕЛЯ 2025 В 10:00</b>
              <b red>20.04.2024 в 10:00</b> -->
            </h2>
            <br />
            <br />
            <!-- <a href="/data/news/Порядок проведения.pdf" class="ab__link" target="_blank"
              >Порядок проведения и ФИО кураторов групп</a
            >  -->
          </div>
          <div class="events__text">
            <img
              alt="День открытых дверей"
              src="/img/organization/photo_2025-10-27_13-09-16.jpg"
              class="openDay" />
            <h2 class="ab__subtitle doors"></h2>
          </div>
        </div>
      </AppBlock>

      <!-- <AppBlock
        :content-style="{
          padding: '24px',
        }"
        class="events__self"
        title="День Знаний">
        <div class="events__text">
          <h2 class="ab__subtitle"><b red>Порядок проведения «Дня Знаний - 1 сентября»</b></h2>
          <p class="ab__p">1 сентября для студентов 1-го курса пройдет общая линейка</p>
          <p class="ab__p">
            После общей линейки для студентов кураторы групп проведут кураторские часы

            <a href="/data/news/Порядок проведения.pdf" class="ab__link" target="_blank"
              >Порядок проведения и ФИО кураторов групп</a
            >
          </p>
        </div>
      </AppBlock> -->

      <!-- <AppBlock
        :content-style="{
          padding: '24px',
        }"
        class="events__self testgipn"
        title="Год семьи">
        <div class="left">
          <swiper :options="swiperOptions">
            <swiper-slide
              ><a href="https://семья2024.рф"
                ><img
                  style="width: 980px; height: auto"
                  class="event__img-main"
                  alt="Events-Image"
                  loading="preload"
                  src="/img/organization/family-year.webp" /> </a
            ></swiper-slide>
          </swiper>
        </div>
      </AppBlock> -->

      <AppBlock
        :content-style="{
          padding: '0',
          background: '#ffff',
          color: 'white',
          overflow: 'hidden',
          position: 'relative',
          borderRadius: '10px',
        }"
        class="kitek-promo-block"
        title="Твой старт в карьеру #ПоступитьПосле9и11Класса">
        <div class="kitek-promo-container" ref="promoContainer">
          <!-- Левый блок с текстом -->
          <div class="kitek-text-content">
            <h2 class="kitek-main-title" ref="mainTitle">
              <span class="title-highlight">КИТЭК</span> - начало твоего успеха!
            </h2>
            <h2 class="kitec-main-title-h2" ref="subTitle1">
              Ты готов изменить свою жизнь и сделать первый шаг к мечте? Начни своё успешное будущее
              уже сегодня!
            </h2>
            <h2 class="kitec-main-title-h2" ref="subTitle2">
              В КИТЭК ты найдёшь не просто знания, а вдохновение, поддержку и дружескую атмосферу!
            </h2>
            <div class="kitek-message-container">
              <div class="kitek-message" ref="message1">
                <div class="message-icon">
                  <!-- Книга (образование) -->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                    <path d="M10 2v20" />
                  </svg>
                </div>
                <p>
                  Поступай в КИТЭК и получи качественное образование, современные знания и
                  практические навыки, которые помогут реализовать твои мечты!
                </p>
              </div>

              <div class="kitek-message" ref="message2">
                <div class="message-icon">
                  <!-- Диплом (профессионализм) -->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                    <polyline points="14 2 14 8 20 8" />
                    <line x1="10" y1="13" x2="14" y2="13" />
                    <line x1="10" y1="17" x2="14" y2="17" />
                    <line x1="8" y1="13" x2="8" y2="13.01" />
                    <line x1="8" y1="17" x2="8" y2="17.01" />
                  </svg>
                </div>
                <p>Поступай в КИТЭК и стань профессионалом в востребованной сфере!</p>
              </div>

              <div class="kitek-message" ref="message3">
                <div class="message-icon">
                  <!-- Шестерёнка (инновации и технологии) -->
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="1.5"
                    stroke-linecap="round"
                    stroke-linejoin="round">
                    <circle cx="12" cy="12" r="3" />
                    <path
                      d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" />
                  </svg>
                </div>
                <p>Поступай в КИТЭК и открой двери в мир, где твои идеи становятся реальностью!</p>
              </div>
            </div>
            <div class="kitek-counter" ref="counter">
              <div class="counter-item">
                <div class="counter-number">11</div>
                <div class="counter-label">Апреля 10:00</div>
              </div>
              <div class="counter-item">
                <div class="counter-number">2026</div>
                <div class="counter-label">года</div>
              </div>
              <div class="counter-description">Единый день открытых дверей</div>
            </div>
          </div>

          <!-- Правый блок с графикой -->
          <div class="kitek-visual-content">
            <div class="floating-elements">
              <div class="floating-card card-1" ref="card1">
                <span
                  ><a href="https://omsktec.ru/enrolle/committee"
                    >Поступить после 9 и 11 классов</a
                  ></span
                >
              </div>
              <div class="floating-card card-2" ref="card2">
                <span
                  ><a href="https://omsktec.ru/enrolle/committee"
                    >Профессии и специальности</a
                  ></span
                >
              </div>
              <div class="floating-card card-3" ref="card3">
                <span
                  ><a href="https://omsktec.ru/enrolle/committee"
                    >Обучение после 9 и 11 классов</a
                  ></span
                >
              </div>
            </div>

            <!-- Необычная 3D кнопка -->
            <a
              href="https://omsktec.ru/enrolle/enrolle-menu"
              class="kitek-3d-button"
              target="_blank"
              rel="noopener noreferrer">
              <span class="button-content">
                <span class="button-front">Поступить сейчас</span>
                <span class="button-back"></span>
                <span class="button-side"></span>
              </span>
            </a>
          </div>
        </div>
      </AppBlock>
      <AppBlock
        :content-style="{
          padding: '24px',
        }"
        class="events__self testgipn"
        title="2025 ГОД ЗАЩИТНИКА ОТЕЧЕСТВА">
        <div class="left">
          <swiper :options="swiperOptions">
            <swiper-slide
              ><a href="https://omsktec.ru/enrolle/enrolle-menu"
                ><img
                  style="width: auto; height: auto"
                  class="event__img-main"
                  alt="Events-Image"
                  loading="preload"
                  src="/img/organization/Bannerpobeda.webp" /> </a
            ></swiper-slide>
          </swiper>
        </div>
      </AppBlock>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
      swiperOptions: {
        grabCursor: true,
        autoplay: {
          enabled: true,
          delay: 6000,
        },
      },
    }
  },

  mounted() {
    this.setupScrollAnimations()
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    setupScrollAnimations() {
      // Добавляем обработчик для анимации при скролле
      this.handleScroll()
    },
    handleScroll() {
      const container = this.$refs.promoContainer
      if (!container) return

      const rect = container.getBoundingClientRect()
      const isVisible = rect.top < window.innerHeight * 0.8 && rect.bottom > 0

      if (isVisible) {
        container.classList.add('visible')

        // Анимируем остальные элементы
        this.animateElement(this.$refs.mainTitle)
        this.animateElement(this.$refs.subTitle1)
        this.animateElement(this.$refs.subTitle2)
        this.animateElement(this.$refs.message1)
        this.animateElement(this.$refs.message2)
        this.animateElement(this.$refs.message3)
        this.animateElement(this.$refs.counter)
        this.animateElement(this.$refs.card1)
        this.animateElement(this.$refs.card2)
        this.animateElement(this.$refs.card3)
        this.animateElement(this.$refs.button)
      }
    },
    animateElement(el) {
      if (el && !el.classList.contains('visible')) {
        el.classList.add('visible')
      }
    },
  },
}

// анимация блока
</script>

<style scoped lang="scss">
.ab {
  &__subtitle {
    font-size: 1.5vw;
    display: grid;
    justify-items: center;
    margin-top: 3vw;
    @media screen and (max-width: 930px) {
      font-size: 18px;
    }
  }
}
.events {
  position: relative;
  display: block;
  justify-content: flex-start;
  margin-bottom: 20px;
  @media screen and (max-width: 930px) {
    // display: none;
  }
  &__self {
    position: relative;
  }

  &__text {
    margin-left: auto;
    margin-right: auto;
    max-width: 50%;
    @media screen and (max-width: 460px) {
      max-width: 1000px;
      height: auto;
    }
  }
  &__left {
    cursor: pointer;
    float: left;
    display: block;
    @media screen and (max-width: 460px) {
      display: none;
    }
  }
  &__right {
    cursor: pointer;
    float: right;
    display: block;
    @media screen and (max-width: 460px) {
      display: none;
    }
  }
}
.event {
  background-color: #fff;
  &__img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin-top: 20px;
    margin-right: 6px;
    border-radius: 50%;
    margin-bottom: 40px;
    @media screen and (max-width: 1460px) {
      width: 100px;
      height: 100px;
    }
    &-main {
      margin-left: auto;
      margin-right: auto;
    }
    &-one {
      display: block;
      @media screen and (max-width: 1460px) {
        width: 100px;
        height: 100px;
      }
      @media screen and (max-width: 930px) {
        display: none;
      }
    }
    &-two {
      display: none;
      @media screen and (max-width: 930px) {
        width: 100px;
        height: 100px;
        display: block;
      }
    }
  }
  &__text {
    @media screen and (max-width: 1360px) {
      margin-top: -10px;
    }
    @media screen and (max-width: 460px) {
      margin-top: -20px;
      max-width: 1000px;
      position: static;
    }
  }
}
.enlarged {
  visibility: visible;
  top: 80px;
  left: 0px;
  position: fixed;
  z-index: 1200;
  width: 100vw;
  height: 100vh;
  background-color: rgba($color: #000000, $alpha: 0.5);
}
.slider {
  position: relative;
  height: 75vh;
  width: 60vw;
  background-color: #fff;
  transition: $t height;
  position: relative;
  @media screen and (max-width: 720px) {
    margin-top: 15vh;
    height: 60vw;
    width: 60vw;
  }
  &__pagination {
    bottom: 10px;
    position: fixed;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1280;
    bottom: 16px !important;
  }
  &__controls {
    right: 24px;
    bottom: 24px;
    display: flex;
    align-items: center;
    z-index: 1300;
  }
  &__close {
    top: 60px;
    right: 50px;
    position: absolute;
  }
  &__next {
    top: 40vh;
    right: 50px;
    position: absolute;
    transform: rotate(-90deg);
  }
  &__prev {
    top: 40vh;
    left: 50px;
    position: absolute;
    margin-right: 12px;
    transform: rotate(90deg);
  }
  &__prev,
  &__close,
  &__next {
    transition: color $t;
    color: $icon-color;
    cursor: pointer;
    &:hover {
      color: $accent-color;
    }
  }
  &__img {
    width: 100%;
    height: 100%;
  }
}

.doors {
  padding-right: 180px;
  margin-top: 30px;
  line-height: 1.5;
}
@media screen and (max-width: 440px) {
  .doors {
    width: 500px;
  }
}
@media screen and (max-width: 930px) {
  .doors {
    width: 500px;
  }
}
// .logo {
//   // position: absolute;
//   width: 255px;
//   height: 230px;
//   right: 13%;
//   top: 75px;

//   @include high-media() {
//     width: 210px;
//     height: auto;
//     right: 12px;
//     top: 60px;
//   }
//   @include small-media() {
//     width: 160px;
//     height: auto;
//     right: 10px;
//     top: 100px;
//   }
// }
.openDay {
  width: auto;
  height: auto;
}
b {
  text-align: center;
}
.opendoors {
  display: flex;
  flex-direction: row;
}
@media screen and (max-width: 745px) {
  .opendoors {
    display: flex;
    flex-direction: column;
  }
  .openDay {
    width: 320px;
    height: auto;
    margin-left: 0;
  }
  .events__text {
    margin-left: 0;
  }
}
.job_fair {
  margin-top: 20px;
  width: 100vw;
  max-height: auto;
  @media screen and (max-width: 640px) {
    display: none;
  }
  &__mobile {
    display: none;
    @media screen and (max-width: 640px) {
      display: block;
      // max-width: 240px;
      max-height: 400px;
      margin-left: auto;
      margin-right: auto;
      // margin-top: 20px;
    }
  }
}

// стили блока

.kitek-promo-block {
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  padding: 0px 15px;
  padding-top: 10px;
}

.kitek-promo-container p,
.kitek-promo-container h2 {
  color: #0e1111;
}
.floating-card {
  color: #0e1111;
}
.counter-description,
.counter-label {
  color: #0e1111;
}

.kitek-promo-container {
  display: flex;
  min-height: 400px;
  padding: 40px;
  position: relative;
  z-index: 2;
  border-radius: 10px;
  border: #c43e3e 3px solid;
}

.kitek-text-content {
  flex: 1;
  padding-right: 40px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.kitek-main-title {
  font-size: 2.5rem;
  margin-bottom: 30px;
  line-height: 1.2;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease;
}

.kitek-main-title.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Голубоватая надпись "КИТЭК" с градиентом */
.title-highlight {
  font-weight: 800;
  background: linear-gradient(90deg, #c43e3e, #c43e3e);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.kitec-main-title-h2 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  line-height: 1.4;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease 0.2s;
}

.kitec-main-title-h2.visible {
  opacity: 1;
  transform: translateY(0);
}

.kitek-message-container {
  margin-bottom: 40px;
}

.kitek-message {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
  opacity: 0;
  transform: translateX(-20px);
  transition: all 0.6s ease;
}

.kitek-message.visible {
  opacity: 1;
  transform: translateX(0);
}

.kitek-message:nth-child(1) {
  transition-delay: 0.4s;
}
.kitek-message:nth-child(2) {
  transition-delay: 0.6s;
}
.kitek-message:nth-child(3) {
  transition-delay: 0.8s;
}

.message-icon {
  font-size: 1.5rem;
  margin-right: 15px;
  flex-shrink: 0;
}

.kitek-counter {
  display: flex;
  align-items: center;
  margin-top: 30px;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease 1s;
}

.kitek-counter.visible {
  opacity: 1;
  transform: translateY(0);
}

.counter-item {
  text-align: center;
  margin-right: 30px;
  position: relative;
}

.counter-item:after {
  content: '';
  position: absolute;
  right: -15px;
  top: 50%;
  transform: translateY(-50%);
  width: 2px;
  height: 30px;
  background: #303030;
}

.counter-item:last-child:after {
  display: none;
}

.counter-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #c43e3e;
  line-height: 1;
}

.counter-label {
  font-size: 0.9rem;
  opacity: 0.8;
}

.counter-description {
  font-size: 1.1rem;
  margin-left: 20px;
  opacity: 0.9;
}

.kitek-visual-content {
  flex: 1;
  position: relative;
  min-height: 300px;
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  padding: 0px 30px;
  box-sizing: border-box;
}

.floating-elements {
  position: absolute;
  width: 100%;
  height: 100%;
}

.floating-card {
  position: absolute;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  padding: 15px 20px;
  font-weight: 500;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  animation: float 6s infinite ease-in-out;
  opacity: 0;
  transition: all 0.6s ease;
}

.floating-card.visible {
  opacity: 1;
}

.floating-card span {
  display: inline-block;
  background: linear-gradient(90deg, #c43e3e, #c43e3e);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.card-1 {
  top: 10%;
  left: 10%;
  animation-delay: 0s;
  transition-delay: 0.4s;
}

.card-2 {
  top: 50%;
  right: 5%;
  animation-delay: 0.5s;
  transition-delay: 0.6s;
}

.card-3 {
  bottom: 15%;
  left: 20%;
  animation-delay: 1s;
  transition-delay: 0.8s;
}

/* кнопка */
/* Основной контейнер кнопки */
.kitek-3d-button {
  display: inline-block;
  position: relative;
  width: 200px;
  height: 60px;
  perspective: 1000px;
  text-decoration: none;
  z-index: 100;
  /* Отключаем все pointer-events для контейнера */
  // pointer-events: none;
}

/* Внутренний контент кнопки - здесь включаем pointer-events */
.kitek-3d-button .button-content {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: all 0.3s ease;
  pointer-events: auto; /* Включаем кликабельность */
  display: block;
}

/* Стили для передней части */
.button-front {
  position: absolute;
  width: 100%;
  height: 100%;
  background: #c43e3e;
  color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  transform: translateZ(15px);
  transition: all 0.3s ease;
  z-index: 3;
  pointer-events: none; /* Отключаем для внутренних элементов */
}

/* Стили для задней части */
.button-back {
  position: absolute;
  width: 100%;
  height: 100%;
  background: #388e3c;
  border-radius: 12px;
  transform: translateZ(-15px);
  transition: all 0.3s ease;
  z-index: 2;
  pointer-events: none;
}

/* Стили для боковой части */
.button-side {
  position: absolute;
  width: 100%;
  height: 30px;
  background: #2e7d32;
  bottom: -15px;
  border-radius: 0 0 12px 12px;
  transform: rotateX(-90deg) translateZ(15px);
  transform-origin: bottom;
  transition: all 0.3s ease;
  z-index: 1;
  pointer-events: none;
}

/* Анимации при наведении */
.kitek-3d-button:hover .button-front {
  transform: translateZ(25px);
}

.kitek-3d-button:hover .button-back {
  transform: translateZ(-25px);
}

.kitek-3d-button:hover .button-side {
  transform: rotateX(-90deg) translateZ(25px);
}

/* Адаптация для мобильных */
@media (max-width: 768px) {
  .kitek-3d-button {
    width: 100%;
    max-width: 300px;
    margin: 20px auto;
  }
}
/* Декоративные элементы */
.kitek-decoration {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  overflow: hidden;
  z-index: 1;
  pointer-events: none;
}

.decoration-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.1;
  transition: all 1s ease;
}

.circle-1 {
  width: 300px;
  height: 300px;
  background: #4caf50;
  top: -100px;
  right: -100px;
  transform: scale(0.8);
}

.circle-2 {
  width: 200px;
  height: 200px;
  background: #ff9800;
  bottom: -50px;
  left: -50px;
  transform: scale(0.8);
}

.kitek-promo-container.visible .decoration-circle {
  transform: scale(1);
}

.decoration-dots {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(rgba(255, 255, 255, 0.1) 1px, transparent 1px);
  background-size: 20px 20px;
  opacity: 0;
  transition: opacity 1s ease 0.5s;
}

.kitek-promo-container.visible .decoration-dots {
  opacity: 1;
}
.message-icon svg {
  width: 24px;
  height: 24px;
  stroke: #000000; /* Чёрный цвет для иконок */
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
/* Анимации */
@keyframes float {
  0%,
  100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-15px) rotate(2deg);
  }
}

/* Адаптивность */
@media (max-width: 768px) {
  .kitek-promo-container {
    flex-direction: column;
    padding: 20px;
  }

  .kitek-text-content {
    padding-right: 0;
    margin-bottom: 30px;
  }

  .kitek-main-title {
    font-size: 1.8rem;
    text-align: center;
  }

  .kitec-main-title-h2 {
    font-size: 1.2rem;
    text-align: center;
  }

  .kitek-visual-content {
    min-height: 200px;
    padding: 20px;
    justify-content: center;
    align-items: center;
  }

  .kitek-3d-button {
    width: 100%;
    max-width: 300px;
    position: relative;
    margin: 0 auto;
  }

  .floating-card {
    position: relative;
    margin: 10px auto;
    width: 80%;
    left: 0;
    right: 0;
    opacity: 1;
  }

  .card-1,
  .card-2,
  .card-3 {
    position: relative;
    top: auto;
    left: auto;
    right: auto;
    bottom: auto;
    margin: 15px auto;
  }
}
</style>
