<template>
  <div class="events">
    <div>
      <AppBlock
        :content-style="{
          padding: '0',
          color: 'white',
          overflow: 'hidden',
          position: 'relative',
          borderRadius: '10px',
        }"
        class="kitek-promo-block"
        title="Твой старт в карьеру #ПоступитьПосле9и11Класса">
        <!-- Оранжевая полоса -->
        <div class="orange-stripe"></div>

        <div class="kitek-promo-container" ref="promoContainer">
          <!-- Левый блок с текстом -->
          <div class="kitek-text-content">
            <h2 class="banner-title">
              КИТЭК
              <span class="highlight-text">начало твоего успеха!</span>
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
                <div class="counter-number">18</div>
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
      this.handleScroll()
    },
    handleScroll() {
      const container = this.$refs.promoContainer
      if (!container) return

      const rect = container.getBoundingClientRect()
      const isVisible = rect.top < window.innerHeight * 0.8 && rect.bottom > 0

      if (isVisible) {
        container.classList.add('visible')

        this.animateElement(this.$refs.subTitle1)
        this.animateElement(this.$refs.subTitle2)
        this.animateElement(this.$refs.message1)
        this.animateElement(this.$refs.message2)
        this.animateElement(this.$refs.message3)
        this.animateElement(this.$refs.counter)
        this.animateElement(this.$refs.card1)
        this.animateElement(this.$refs.card2)
        this.animateElement(this.$refs.card3)
      }
    },
    animateElement(el) {
      if (el && !el.classList.contains('visible')) {
        el.classList.add('visible')
      }
    },
  },
}
</script>

<style scoped lang="scss">
// Основная палитра
$kitek-red: #c43e3e;
$kitek-dark-red: #a12f2f;
$text-black: #1a1a1a;
$text-gray: #4a4a4a;

// Оранжевая полоса
.orange-stripe {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: $kitek-red;
  z-index: 10;
}

.kitek-promo-block {
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid #eeeeee;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
  position: relative;
}

.banner-title {
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1.2;
  color: #1a1a1a;
  margin-bottom: 25px;
  margin-top: 15px;

  .highlight-text {
    display: block;
    color: #c43e3e;
    font-size: 2.8rem;
    margin-top: 5px;
    position: relative;
    padding-left: 20px;

    &::before {
      content: '';
      position: absolute;
      left: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 8px;
      height: 80%;
      background: linear-gradient(to bottom, #c43e3e, #c43e3e);
      border-radius: 4px;
    }
  }
}

.title-h2 {
  font-size: 30px;
  font-weight: bold;
  color: #c43e3e;
}

.kitek-promo-container {
  display: flex;
  min-height: 480px;
  padding: 50px;
  padding-top: 54px; // Добавляем отступ сверху для полосы
  position: relative;
  overflow: hidden;
  background: #ffffff;
}

.kitek-text-content {
  flex: 1.2;
  position: relative;
  z-index: 10;
}

.kitec-main-title-h2 {
  font-size: 1.1rem;
  color: $text-gray;
  line-height: 1.6;
  margin-bottom: 15px;
  font-weight: 400;
  opacity: 0;
  transition: opacity 0.6s ease 0.3s;

  &.visible {
    opacity: 1;
  }
}

.kitek-message-container {
  margin-bottom: 35px;
}

.kitek-message {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 15px;
  opacity: 0;
  transform: translateX(-15px);
  transition: all 0.5s ease;

  &.visible {
    opacity: 1;
    transform: translateX(0);
  }

  p {
    font-size: 0.95rem;
    color: $text-black;
    margin: 0;
    line-height: 1.4;
  }

  .message-icon {
    flex-shrink: 0;
    margin-top: 2px;
    svg {
      stroke: $kitek-red !important;
      width: 20px;
      height: 20px;
    }
  }
}

.kitek-counter {
  display: flex;
  align-items: center;
  gap: 25px;
  margin-top: 20px;
  opacity: 0;
  transition: opacity 0.8s ease 0.6s;

  &.visible {
    opacity: 1;
  }

  .counter-item {
    .counter-number {
      font-size: 2.2rem;
      font-weight: 800;
      color: $kitek-red;
      line-height: 1;
    }
    .counter-label {
      font-size: 0.8rem;
      color: #999;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
  }

  .counter-description {
    font-size: 0.95rem;
    color: $text-gray;
    border-left: 1px solid #e0e0e0;
    padding-left: 20px;
    max-width: 150px;
  }
}

// Правая часть
.kitek-visual-content {
  flex: 0.8;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-end;
}

.floating-elements {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.floating-card {
  position: absolute;
  background: #ffffff;
  padding: 12px 20px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.07);
  border: 1px solid #f0f0f0;
  pointer-events: auto;
  opacity: 0;
  animation: float-animation 5s infinite ease-in-out;
  transition: opacity 0.8s ease;

  &.visible {
    opacity: 1;
  }

  a {
    text-decoration: none;
    font-weight: 600;
    color: $kitek-red;
    font-size: 0.85rem;
  }

  &:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  }
}

// Позиции карточек
.card-1 {
  top: 10%;
  right: 20%;
  animation-delay: 0s;
  transition-delay: 0.4s;
}
.card-2 {
  top: 35%;
  right: 5%;
  animation-delay: 1s;
  transition-delay: 0.6s;
}
.card-3 {
  top: 60%;
  right: 25%;
  animation-delay: 2s;
  transition-delay: 0.8s;
}

// Кнопка 3D
.kitek-3d-button {
  display: block;
  width: 220px;
  height: 56px;
  text-decoration: none;
  perspective: 1000px;
  margin-bottom: 20px;

  .button-content {
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.2s ease;
  }

  .button-front {
    position: absolute;
    inset: 0;
    background: $kitek-red;
    color: #ffffff;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 1rem;
    transform: translateZ(15px);
    box-shadow: 0 6px 15px rgba($kitek-red, 0.3);
  }

  .button-side {
    position: absolute;
    width: 100%;
    height: 15px;
    background: $kitek-dark-red;
    bottom: -8px;
    left: 0;
    border-radius: 0 0 10px 10px;
    transform: rotateX(-90deg) translateZ(8px);
  }

  &:hover .button-content {
    transform: rotateX(15deg);
  }

  &:active .button-content {
    transform: translateY(3px) rotateX(0deg);
  }
}

@keyframes float-animation {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

// Адаптивность
@media (max-width: 992px) {
  .kitek-promo-container {
    padding: 40px;
    padding-top: 44px;
  }
}

@media (max-width: 768px) {
  .kitek-promo-container {
    flex-direction: column;
    padding: 30px 20px;
    padding-top: 34px;
    min-height: auto;
    text-align: center;
  }

  .kitek-text-content {
    padding-right: 0;
  }

  .floating-elements {
    display: none;
  }

  .kitek-message {
    text-align: left;
    background: #fcfcfc;
    padding: 10px;
    border-radius: 8px;
  }

  .kitek-counter {
    justify-content: center;
    flex-wrap: wrap;
    .counter-description {
      border-left: none;
      padding: 0;
      max-width: 100%;
      width: 100%;
    }
  }

  .kitek-visual-content {
    align-items: center;
    margin-top: 30px;
  }

  .kitek-3d-button {
    width: 100%;
    max-width: 280px;
    margin: 0 auto;
  }
}
</style>
