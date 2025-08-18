<template>
  <div class="slider">
    <h1 class="slider__kitek">Колледж инновационных технологий, экономики и коммерции</h1>
    <swiper :options="swiperOptions" class="slider">
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Доступное образование</h1>
              <h2 class="slide__subtitle">
                Востребованные образовательные программы и освоение новой за короткое время, в
                удобном формате
              </h2>
              <h2 class="slide__subtitle__mobile">Востребованные образовательные программы</h2>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>

            <div class="slide__imgs">
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                loading="preload"
                src="/img/sliders/1.webp" />
              <img
                class="slide__img"
                alt="Slider-Image"
                loading="preload"
                src="/img/sliders/1.webp" />
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                loading="preload"
                src="/img/sliders/1.webp" />
            </div>

            <!-- Absolute -->
            <IconWrapper class="abs abs__left" width="64" height="64">
              <IconCakeSwirl />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="64" height="64">
              <IconCakeSwirl />
            </IconWrapper>
            <IconWrapper class="abs abs__center" width="48" height="48">
              <IconCake />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Наставничество и менторинг</h1>
              <h2 class="slide__subtitle">
                Квалифицированные специалисты, опыт наставников, практикующие эксперты
              </h2>
              <h2 class="slide__subtitle__mobile">Квалифицированные специалисты</h2>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                src="/img/sliders/2.webp"
                loading="lazy" />

              <img class="slide__img" alt="Slider-Image" src="/img/sliders/2.webp" loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Устойчивые традиции</h1>
              <h2 class="slide__subtitle">
                Уважение к прошлому, ответственное отношение к настоящему, четкое видение будущего
              </h2>
              <h2 class="slide__subtitle__mobile">
                Уважение к прошлому, ответственное отношение к настоящему
              </h2>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                src="/img/sliders/cook.webp"
                loading="lazy" />
              <img
                class="slide__img"
                alt="Slider-Image"
                src="/img/sliders/cook.webp"
                loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="64" height="64">
              <IconCakeSwirl />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="64" height="64">
              <IconCakeSwirl />
            </IconWrapper>
            <IconWrapper class="abs abs__center" width="48" height="48">
              <IconCake />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Бизнес-старт для начинающих</h1>
              <h2 class="slide__subtitle">
                Возможность стать владельцем собственного бизнеса, самозанятым через программы
                бизнес-обучения
              </h2>
              <h2 class="slide__subtitle__mobile">
                Возможность стать владельцем собственного бизнеса
              </h2>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                src="/img/sliders/business.webp"
                loading="lazy" />
              <img
                class="slide__img"
                alt="Slider-Image"
                src="/img/sliders/business.webp"
                loading="lazy" />
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                src="/img/sliders/business.webp"
                loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Студенческое сообщество</h1>
              <h2 class="slide__subtitle">
                3000 студентов, которые вместе на занятиях и в свободное время
              </h2>
              <h2 class="slide__subtitle__mobile">
                3000 студентов, которые вместе на занятиях и в свободное время
              </h2>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                src="/img/sliders/student.webp"
                loading="lazy" />
              <img
                class="slide__img"
                alt="Slider-Image"
                src="/img/sliders/student.webp"
                loading="lazy" />
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                src="/img/sliders/student.webp"
                loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Развитое социальное партнерство</h1>
              <h2 class="slide__subtitle">
                100% успешное трудоустройство выпускников, развитие и профессиональный рост молодых
                специалистов
              </h2>
              <h2 class="slide__subtitle__mobile">
                100% успешное трудоустройство выпускников, развитие и профессиональный рост молодых
                специалистов
              </h2>
              <a href="https://vk.com/trudkitek" target="_blank" class="slide__additional"
                >Подробнее</a
              >
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                src="/img/sliders/tx.webp"
                loading="lazy" />
              <img
                class="slide__img"
                alt="Slider-Image"
                src="/img/sliders/tx.webp"
                loading="lazy" />
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                src="/img/sliders/tx.webp"
                loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Мобильное приложение</h1>
              <h2 class="slide__subtitle">
                Удобное расписание занятий в виде мобильного приложения
              </h2>
              <h2 class="slide__subtitle__mobile">
                Удобное расписание занятий в виде мобильного приложения
              </h2>
              <a href="https://app.omsktec.ru" target="_blank" class="slide__additional"
                >Подробнее</a
              >
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                src="/img/sliders/mobile-app.webp"
                loading="lazy" />
              <img
                class="slide__img"
                alt="Slider-Image"
                src="/img/sliders/mobile-app.webp"
                loading="lazy" />
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                src="/img/sliders/mobile-app.webp"
                loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Непрерывное самообразование</h1>
              <h2 class="slide__subtitle">
                Обучающиеся и педагоги ежегодно участвуют в Национальных чемпионатах професиионалов,
                Всероссийских профессиональных конкурсах и олимпиадах
              </h2>
              <h2 class="slide__subtitle__mobile">
                Обучающиеся и педагоги ежегодно участвуют в Национальных чемпионатах профессионалов,
                Всероссийских профессиональных конкурсах и олимпиадах
              </h2>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img
                class="slide__img slide__img-down"
                alt="Slider-Image"
                src="/img/sliders/self-education.webp"
                loading="lazy" />
              <img
                class="slide__img"
                alt="Slider-Image"
                src="/img/sliders/self-education.webp"
                loading="lazy" />
              <img
                class="slide__img slide__img-up"
                alt="Slider-Image"
                src="/img/sliders/self-education.webp"
                loading="lazy" />
            </div>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <swiper-slide>
        <div class="slide">
          <div class="slide__group">
            <div class="slide__info">
              <h1 class="slide__title">Принципы БПОУ «КИТЭК»</h1>
              <h2 class="slide__subtitle">12 основополагающих принципов БПОУ «КИТЭК»</h2>
              <h2 class="slide__subtitle__mobile">12 основопологащих принципов БПОУ «КИТЭК»</h2>
              <a href="/images" style="cursor: pointer" class="slide__additional">Подробнее</a>
              <a class="ab__link" href="https://япроф.рф/"
                ><img
                  alt="Logo"
                  target="_blank"
                  src="/img/professional/ЛогоПроф2024.png"
                  class="logo"
              /></a>
            </div>
            <div class="slide__imgs">
              <img class="el__img" alt="Slider-Image" src="/img/sliders/logo.png" loading="lazy" />
            </div>
            <IconWrapper class="abs abs__right" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
            <IconWrapper class="abs abs__left" width="48" height="48">
              <IconTaskApproved />
            </IconWrapper>
          </div>
        </div>
      </swiper-slide>
      <div class="slider__pagination" slot="pagination" />
    </swiper>
    <div class="slider__controls">
      <icon-wrapper width="48" height="48" class="slider__prev">
        <icon-circle-arrow />
      </icon-wrapper>
      <icon-wrapper width="48" height="48" class="slider__next">
        <icon-circle-arrow />
      </icon-wrapper>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlockSlider',
  data() {
    return {
      swiperOptions: {
        grabCursor: true,
        pagination: {
          el: '.slider__pagination',
          bulletClass: 'swiper__bullet',
          bulletActiveClass: 'swiper__bullet-active',
        },
        navigation: {
          nextEl: '.slider__next',
          prevEl: '.slider__prev',
        },
        autoplay: {
          enabled: true,
          delay: 7000, //-> 7s
        },
      },
    }
  },
}
</script>

<style scoped lang="scss">
.slider {
  margin-top: 10px;
  height: 460px;
  width: 100%;
  background-color: #fff;
  transition: $t height;
  position: relative;
  &__kitek {
    position: absolute;
    @include tg(20px, 700, 22px);
    color: $accent-color;
    left: 24px;
    top: 24px;
    z-index: 100;
    opacity: 0.4;
    text-align: center;
    width: 100%;
    margin-top: -17px;
  }
  &__pagination {
    position: absolute;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    bottom: 16px !important;
  }
  &__controls {
    position: absolute;
    right: 24px;
    bottom: 24px;
    display: flex;
    align-items: center;
    z-index: 1100;
  }
  &__next {
    transform: rotate(-90deg);
  }
  &__prev {
    margin-right: 12px;
    transform: rotate(90deg);
  }
  &__prev,
  &__next {
    transition: color $t;
    color: $icon-color;
    cursor: pointer;
    &:hover {
      color: $accent-color;
    }
  }
  @include medium-media {
    height: 330px;
    &__pagination {
      justify-content: flex-start;
      margin-left: 16px;
    }
    &__controls {
      right: unset;
      left: 12px;
      bottom: 32px;
    }
    &__prev,
    &__next {
      min-width: 32px !important;
      min-height: 32px !important;
      width: 32px !important;
      height: 32px !important;
    }
    &__prev {
      margin-right: 6px;
    }
    &__kitek {
      display: none;
    }
  }
  @include small-medium-media {
    height: 300px;
  }
}

// refactor needed
.slide {
  background-color: #fff;
  padding: 70px 160px;
  height: 100%;
  width: 100%;
  position: relative;
  @include small-medium-media {
    padding: 24px 40px;
  }
  &__title {
    @extend %tg-slide-title;
    color: $accent-color;
    @include medium-media {
      font-size: 24px;
    }
  }
  &__additional {
    color: $primary-color;
    text-decoration: underline;
    text-underline-offset: 2px;
    font-size: 19px;
  }
  &__subtitle {
    @extend %tg-slide-subtitle;
    margin-top: 24px;
    max-width: 450px;
    min-height: 150px;
    color: $primary-text-color;
    &__mobile {
      @extend %tg-slide-subtitle;
      display: none;
      font-size: 16px;
      margin-top: 12px;
      max-width: 270px;
      min-height: 130px;
      @include small-medium-media {
        display: block;
      }
    }
    @include medium-media {
      font-size: 20px;
      margin-top: 12px;
    }
    @include small-medium-media {
      display: none;
    }
  }
  &__imgs {
    display: flex;
    @include small-medium-media {
      display: block;
      margin-top: 16px;
    }
  }
  &__img {
    width: 300px;
    height: 300px;
    object-fit: cover;
    margin-right: 12px;
    flex: none;
    border-radius: 50%;
    &-down,
    &-up {
      width: 128px;
      height: 128px;
      @include high-media {
        display: none;
      }
    }
    &-down {
      align-self: flex-end;
    }
    @include medium-media {
      width: 200px;
      height: 200px;
    }
    @include small-medium-media {
      width: 150px;
      height: 150px;
      position: absolute;
      right: -10px;
      bottom: 5px;
    }
  }
  &__group {
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 100%;
    @include small-medium-media {
      display: block;
    }
  }
  &__info {
    user-select: none;
  }
}

.cake {
  position: absolute;
}

.abs {
  position: absolute;
  color: $accent-color;
  opacity: 0.5;
  &__left {
    left: 32px;
    bottom: 32px;
  }
  &__right {
    right: 32px;
    top: 32px;
  }
  &__center {
    @include medium-media {
      display: none;
    }
  }
  @include small-medium-media {
    display: none;
  }
}
.el {
  &__img {
    height: 400px;
    width: 400px;
    margin-right: 100px;
    object-fit: cover;
    border-radius: 50%;

    // @keyframes circle-rotation {
    //   0% {
    //     transform: rotate(0deg) translate(0px, 0px);
    //   }
    //   50% {
    //     transform: rotate(3deg) translate(-8px, -10px);
    //   }
    //   100% {
    //     transform: rotate(-1deg) translate(1px, 1px);
    //   }
    // }
    // transform-origin: 50% 50%;
    // animation: circle-rotation 10s ease-in-out infinite alternate;

    @include medium-media {
      right: 50px;
      width: 300px;
      height: 300px;
      display: flex;
    }

    @include small-medium-media {
      width: 220px;
      height: 220px;
    }
    @include small-medium-media {
      width: 200px;
      height: 200px;
      position: absolute;
      right: -10px;
      bottom: 5px;
      margin: 0;
      // animation: none;
    }
  }
}
.logo {
  width: 200px;
  height: 180px;
  right: 23%;
  top: 24px;

  @include high-media() {
    width: 200px;
    height: 170px;
    right: 12px;
    top: 12px;
    position: absolute;
  }
  @include small-media() {
    width: 100px;
    height: 90px;
    right: 240px;
    top: 130px;
  }
}
</style>
