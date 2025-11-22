<template>
  <div class="main-wrapper">
    <!-- Основной слайдер -->
    <div class="slider-container">
      <h1 class="slider-title">Колледж инновационных технологий, экономики и коммерции</h1>
      <swiper :options="swiperOptions" class="main-slider">
        <!-- Слайд 1 - Доступное образование -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Доступное образование</h2>
                <p>
                  Востребованные образовательные программы и освоение новой за короткое время, в
                  удобном формате
                </p>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/1.webp" alt="Образование" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 2 - Наставничество и менторинг -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Наставничество и менторинг</h2>
                <p>Квалифицированные специалисты, опыт наставников, практикующие эксперты</p>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/2.webp" alt="Наставничество" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 3 - Устойчивые традиции -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Устойчивые традиции</h2>
                <p>
                  Уважение к прошлому, ответственное отношение к настоящему, четкое видение будущего
                </p>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/cook.webp" alt="Традиции" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 4 - Бизнес-старт для начинающих -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Бизнес-старт для начинающих</h2>
                <p>
                  Возможность стать владельцем собственного бизнеса, самозанятым через программы
                  бизнес-обучения
                </p>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/business.webp" alt="Бизнес" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 5 - Студенческое сообщество -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Студенческое сообщество</h2>
                <p>3000 студентов, которые вместе на занятиях и в свободное время</p>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/student.webp" alt="Студенты" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 6 - Развитое социальное партнерство -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Развитое социальное партнерство</h2>
                <p>
                  100% успешное трудоустройство выпускников, развитие и профессиональный рост
                  молодых специалистов
                </p>
                <a href="https://vk.com/trudkitek" class="slide-link" target="_blank">
                  <span>Подробнее</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                    <path
                      d="M5 12H19M19 12L12 5M19 12L12 19"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round" />
                  </svg>
                </a>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/tx.webp" alt="Партнерство" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 7 - Мобильное приложение -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Мобильное приложение</h2>
                <p>Удобное расписание занятий в виде мобильного приложения</p>
                <a href="https://app.omsktec.ru" class="slide-link" target="_blank">
                  <span>Подробнее</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                    <path
                      d="M5 12H19M19 12L12 5M19 12L12 19"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round" />
                  </svg>
                </a>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/mobile-app.webp" alt="Приложение" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 8 - Непрерывное самообразование -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Непрерывное самообразование</h2>
                <p>
                  Обучающиеся и педагоги ежегодно участвуют в Национальных чемпионатах
                  профессионалов, Всероссийских профессиональных конкурсах и олимпиадах
                </p>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/self-education.webp" alt="Самообразование" />
              </div>
            </div>
          </div>
        </swiper-slide>

        <!-- Слайд 9 - Принципы БПОУ «КИТЭК» -->
        <swiper-slide>
          <div class="slide-content">
            <div class="text-side">
              <div class="text-content">
                <h2>Принципы БПОУ «КИТЭК»</h2>
                <p>12 основополагающих принципов БПОУ «КИТЭК»</p>
                <a href="/images" class="slide-link">
                  <span>Подробнее</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                    <path
                      d="M5 12H19M19 12L12 5M19 12L12 19"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round" />
                  </svg>
                </a>
              </div>
            </div>
            <div class="image-side">
              <div class="image-container">
                <img src="/img/sliders/logo.png" alt="Принципы" />
              </div>
            </div>
          </div>
        </swiper-slide>
      </swiper>

      <!-- Элементы управления -->
      <div class="slider-controls">
        <div class="slider-pagination"></div>
        <div class="slider-nav">
          <button class="slider-prev">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path
                d="M15 18L9 12L15 6"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </button>
          <button class="slider-next">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path
                d="M9 18L15 12L9 6"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Боковые блоки -->
    <div class="side-blocks">
      <a href="https://app.omsktec.ru" class="side-block schedule-block">
        <div class="block-content">
          <div class="block-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
              <path
                d="M8 2V6M16 2V6M3 10H21M5 4H19C20.1046 4 21 4.89543 21 6V20C21 21.1046 20.1046 22 19 22H5C3.89543 22 3 21.1046 3 20V6C3 4.89543 3.89543 4 5 4Z"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </div>
          <h3>Расписание</h3>
          <p>Мобильное приложение</p>
        </div>
      </a>

      <a href="https://япроф.рф/" class="side-block prof-block">
        <div class="block-content">
          <img src="/img/professional/ЛогоПроф2024.png" alt="Профессионалитет" class="block-logo" />
          <h3>Профессионалитет</h3>
          <p>Образовательные программы</p>
        </div>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModernSlider',
  data() {
    return {
      swiperOptions: {
        pagination: {
          el: '.slider-pagination',
          clickable: true,
          bulletClass: 'swiper-bullet',
          bulletActiveClass: 'swiper-bullet-active',
        },
        navigation: {
          nextEl: '.slider-next',
          prevEl: '.slider-prev',
        },
        autoplay: {
          delay: 5000,
        },
        effect: 'fade',
        fadeEffect: {
          crossFade: true,
        },
        speed: 800,
      },
    }
  },
}
</script>

<style scoped>
/* Основные цвета */
:root {
  --primary-red: #c43e3e;
  --title-red: #d65460;
  --primary-white: #ffffff;
  --primary-gray: #f5f5f5;
  --dark-gray: #333333;
  --light-gray: #e0e0e0;
  --text-gray: #666666;
  --button-red: #b53535;
  --button-hover: #9c2d2d;
  --accent-glow: rgba(196, 62, 62, 0.1);
}

.main-wrapper {
  display: flex;
  gap: 24px;
  margin: 16px auto;
  width: 95%;
  max-width: 1800px;
  height: 480px;
  background: var(#ffffff);
  border-radius: 24px;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.12), 0 2px 8px rgba(0, 0, 0, 0.06);
  padding: 0;
  overflow: hidden;
  position: relative;
}

.main-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, #c43e3e, transparent);
  opacity: 0.3;
}

/* Основной слайдер */
.slider-container {
  flex: 1;
  background: #ffffff;
  position: relative;
  overflow: hidden;
  min-width: 0;
}

.slider-title {
  position: absolute;
  top: 24px;
  left: 0;
  right: 0;
  text-align: center;
  font-size: 16px;
  font-weight: 600;
  color: #d65461;
  opacity: 0.9;
  z-index: 10;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.main-slider {
  height: 100%;
  width: 100%;
}

.slide-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  padding: 80px 60px 60px;
  max-width: 1600px;
  margin: 0 auto;
  position: relative;
}

.text-side {
  flex: 1;
  max-width: 55%;
  padding-right: 60px;
  position: relative;
}

.text-content {
  position: relative;
  z-index: 2;
}

.text-side h2 {
  color: #c43e3e;
  font-size: clamp(32px, 4vw, 52px);
  font-weight: 800;
  margin-bottom: 24px;
  line-height: 1.1;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #c43e3e 0%, #d65460 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.text-side p {
  color: #666666;
  font-size: clamp(16px, 1.8vw, 20px);
  line-height: 1.7;
  font-weight: 400;
  max-width: 600px;
  margin-bottom: 32px;
  position: relative;
  padding-left: 16px;
}

.text-side p::before {
  content: '';
  position: absolute;
  left: 0;
  top: 8px;
  bottom: 8px;
  width: 3px;
  background: linear-gradient(to bottom, #c43e3e, transparent);
  border-radius: 2px;
}

/* Ссылка "Подробнее" */
.slide-link {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 14px 32px;
  background: linear-gradient(135deg, #b53535 0%, #c43e3e 100%);
  color: white;
  text-decoration: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 16px;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  border: none;
  box-shadow: 0 4px 15px rgba(181, 53, 53, 0.3), 0 2px 4px rgba(181, 53, 53, 0.2);
  position: relative;
  overflow: hidden;
}

.slide-link::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.6s ease;
}

.slide-link:hover {
  background: linear-gradient(135deg, #9c2d2d 0%, #b53535 100%);
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(181, 53, 53, 0.4), 0 4px 8px rgba(181, 53, 53, 0.3);
  color: white;
}

.slide-link:hover::before {
  left: 100%;
}

.slide-link:active {
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(181, 53, 53, 0.4);
}

.slide-link svg {
  transition: transform 0.3s ease;
}

.slide-link:hover svg {
  transform: translateX(4px);
}

.image-side {
  flex: 1;
  text-align: center;
  position: relative;
  max-width: 45%;
}

.image-container {
  position: relative;
  display: inline-block;
}

.image-side::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(420px, 36vw);
  height: min(420px, 36vw);
  background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
  border-radius: 50%;
  z-index: -1;
  box-shadow: inset 0 4px 8px rgba(255, 255, 255, 0.8), 0 8px 32px rgba(0, 0, 0, 0.1);
}

.image-side img {
  width: min(380px, 34vw);
  height: min(380px, 34vw);
  object-fit: cover;
  border-radius: 50%;
  box-shadow: 0 16px 40px rgba(196, 62, 62, 0.2), 0 8px 16px rgba(196, 62, 62, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.8);
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  filter: brightness(1.05) contrast(1.1);
}

/* Управление слайдером */
.slider-controls {
  position: absolute;
  bottom: 32px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 60px;
  z-index: 10;
  max-width: 1600px;
  margin: 0 auto;
}

.slider-nav {
  display: flex;
  gap: 16px;
}

.slider-prev,
.slider-next {
  background: #ffffff;
  color: #c43e3e;
  border: 2px solid #c43e3e;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15), 0 2px 4px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;
}

.slider-prev::before,
.slider-next::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(196, 62, 62, 0.1), transparent);
  transition: left 0.5s ease;
}

.slider-prev:hover,
.slider-next:hover {
  background: #c43e3e;
  color: #ffffff;
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 25px rgba(196, 62, 62, 0.4), 0 4px 8px rgba(196, 62, 62, 0.3);
}

.slider-prev:hover::before,
.slider-next:hover::before {
  left: 100%;
}

/* Пагинация */
.slider-pagination {
  display: flex;
  gap: 10px;
  padding: 8px 16px;

  border-radius: 20px;
  backdrop-filter: blur(10px);
}

:deep(.swiper-bullet) {
  width: 12px;
  height: 12px;
  background: #e0e0e0;
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  position: relative;
  overflow: hidden;
}

:deep(.swiper-bullet)::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.8), transparent);
  transition: left 0.5s ease;
}

:deep(.swiper-bullet-active) {
  background: #c43e3e;
  width: 36px;
  border-radius: 18px;
  box-shadow: 0 2px 8px rgba(196, 62, 62, 0.4);
}

:deep(.swiper-bullet-active)::before {
  left: 100%;
}

:deep(.swiper-bullet:hover) {
  transform: scale(1.2);
}

:deep(.swiper-bullet:hover)::before {
  left: 100%;
}

/* Боковые блоки */
.side-blocks {
  display: flex;
  flex-direction: column;
  gap: 24px;
  width: 320px;
  min-width: 320px;
  padding: 32px;
  background: linear-gradient(135deg, #f5f5f5 0%, #f0f0f0 100%);
  border-radius: 0 24px 24px 0;
  position: relative;
}

.side-blocks::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, #c43e3e, transparent);
  opacity: 0.3;
}

.side-block {
  flex: 1;
  background: #ffffff;
  border-radius: 20px;
  padding: 32px;
  text-decoration: none;
  color: inherit;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  border: 1px solid #e0e0e0;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.04);
}

.side-block::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #c43e3e, #d65460);
  transform: scaleX(0);
  transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  transform-origin: left;
}

.side-block::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
  transition: left 0.6s ease;
}

.side-block:hover {
  transform: translateY(-6px) scale(1.02);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15), 0 8px 16px rgba(0, 0, 0, 0.1);
}

.side-block:hover::before {
  transform: scaleX(1);
}

.side-block:hover::after {
  left: 100%;
}

.schedule-block {
  background: #ffffff;
}

.prof-block {
  background: #ffffff;
}

.block-content {
  text-align: center;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 20px;
  position: relative;
  z-index: 2;
}

.block-icon {
  width: 72px;
  height: 72px;

  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2e2e2e;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  box-shadow: 0 4px 15px rgba(215, 92, 92, 0.192);
}

.block-logo {
  height: 72px;
  width: auto;
  object-fit: contain;
  transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

.side-block:hover .block-logo {
  transform: scale(1.1);
  filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.15));
}

.block-content h3 {
  margin: 0;
  font-size: 20px;
  font-weight: 700;
  color: #333333;
  letter-spacing: -0.2px;
}

.block-content p {
  margin: 0;
  font-size: 16px;
  color: #666666;
  line-height: 1.4;
}

/* Адаптивность для кнопки */
@media (max-width: 1023px) and (min-width: 768px) {
  .slide-link {
    padding: 12px 24px;
    font-size: 15px;
  }
}

@media (max-width: 767px) {
  .slide-link {
    padding: 10px 20px;
    font-size: 14px;
    border-radius: 10px;
  }

  .slide-link svg {
    width: 14px;
    height: 14px;
  }
}

@media (max-width: 480px) {
  .slide-link {
    padding: 8px 16px;
    font-size: 13px;
    border-radius: 8px;
  }
}

/* Большие экраны (1440px+) */
@media (min-width: 1440px) {
  .main-wrapper {
    height: 520px;
  }

  .slide-content {
    padding: 90px 80px 70px;
    padding-right: 0px;
  }

  .text-side {
    padding-right: 80px;
  }

  .side-blocks {
    width: 360px;
    min-width: 360px;
    padding: 40px;
  }

  .side-block {
    border: 1px solid #c43e3e40;
  }
}

/* Очень большие экраны (1920px+) */
@media (min-width: 1920px) {
  .main-wrapper {
    height: 580px;
    max-width: 2000px;
  }

  .slide-content {
    padding: 100px 100px 80px;
  }

  .text-side h2 {
    font-size: 56px;
  }

  .text-side p {
    font-size: 22px;
  }

  .side-blocks {
    width: 400px;
    min-width: 400px;
  }

  .side-block {
    border: 1px solid #c43e3e40;
  }

  .block-content h3 {
    font-size: 22px;
  }

  .block-content p {
    font-size: 18px;
  }
}

/* Ноутбуки (1024px - 1439px) */
@media (max-width: 1439px) and (min-width: 1024px) {
  .main-wrapper {
    height: 440px;
  }

  .slide-content {
    padding: 70px 50px 50px;
  }

  .text-side {
    padding-right: 40px;
  }

  .slider-controls {
    padding: 0 50px;
    bottom: 28px;
  }
  .side-block {
    border: 1px solid #c43e3e40;
  }
}

/* Планшеты и маленькие ноутбуки (768px - 1023px) */
@media (max-width: 1023px) and (min-width: 768px) {
  .main-wrapper {
    flex-direction: column;
    height: auto;
    gap: 0;
    margin: 12px;
    border-radius: 20px;
    width: calc(100% - 24px);
  }

  .slider-container {
    height: 400px;
    border-radius: 20px 20px 0 0;
  }

  .side-blocks {
    flex-direction: row;
    width: 100%;
    min-width: auto;
    padding: 24px;
    border-radius: 0 0 20px 20px;
    gap: 20px;
  }

  .slide-content {
    flex-direction: column;
    padding: 70px 40px 40px;
    text-align: center;
    max-width: none;
  }

  .text-side {
    max-width: 100%;
    margin-bottom: 30px;
    padding-right: 0;
  }

  .text-side h2 {
    font-size: 34px;
  }

  .text-side p::before {
    display: none;
  }

  .text-side p {
    padding-left: 0;
  }

  .image-side {
    max-width: none;
  }

  .image-side::before {
    width: 240px;
    height: 240px;
  }

  .image-side img {
    width: 200px;
    height: 200px;
  }

  .slider-title {
    font-size: 14px;
    top: 20px;
  }

  .side-block {
    padding: 24px;
  }

  .block-content {
    gap: 16px;
  }

  .block-icon {
    width: 56px;
    height: 56px;
    border-radius: 16px;
  }

  .block-icon svg {
    width: 24px;
    height: 24px;
  }

  .block-logo {
    height: 56px;
  }

  .block-content h3 {
    font-size: 18px;
  }

  .block-content p {
    font-size: 14px;
  }

  .slider-controls {
    bottom: 24px;
    padding: 0 40px;
  }

  .slider-prev,
  .slider-next {
    width: 48px;
    height: 48px;
  }
}

/* Мобильные устройства (до 767px) */
@media (max-width: 767px) {
  .main-wrapper {
    flex-direction: column;
    height: auto;
    gap: 0;
    margin: 8px;
    border-radius: 16px;
    width: calc(100% - 16px);
  }

  .slider-container {
    height: 380px;
    border-radius: 16px 16px 0 0;
  }

  .side-blocks {
    flex-direction: row;
    width: 100%;
    min-width: auto;
    padding: 16px;
    border-radius: 0 0 16px 16px;
    gap: 12px;
  }

  .slide-content {
    flex-direction: column;
    padding: 60px 24px 24px;
    text-align: center;
    max-width: none;
  }

  .text-side {
    max-width: 100%;
    margin-bottom: 24px;
    padding-right: 0;
  }

  .text-side h2 {
    font-size: 30px;
  }

  .text-side p {
    font-size: 16px;
    margin-bottom: 20px;
  }

  .text-side p::before {
    display: none;
  }

  .text-side p {
    padding-left: 0;
  }

  .image-side {
    max-width: none;
  }

  .image-side::before {
    width: 180px;
    height: 180px;
  }

  .image-side img {
    width: 150px;
    height: 150px;
  }

  .slider-title {
    display: none;
  }

  .side-block {
    padding: 20px 16px;
    border-radius: 16px;
  }

  .block-content {
    gap: 12px;
  }

  .block-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
  }

  .block-icon svg {
    width: 20px;
    height: 20px;
  }

  .block-logo {
    height: 48px;
  }

  .block-content h3 {
    font-size: 16px;
  }

  .block-content p {
    font-size: 12px;
  }

  .slider-controls {
    bottom: 20px;
    padding: 0 24px;
  }

  .slider-prev,
  .slider-next {
    width: 44px;
    height: 44px;
  }

  .slider-pagination {
    display: none;
  }

  .slider-controls {
    justify-content: flex-end;
  }
}

/* Очень маленькие мобильные (до 480px) */
@media (max-width: 480px) {
  .slide-content {
    padding: 50px 16px 16px;
  }

  .text-side {
    text-align: left;
  }
  .text-side h2 {
    font-size: 28px;
  }

  .text-side p {
    font-size: 14px;
    margin-bottom: 16px;
  }

  .side-block {
    padding: 16px 12px;
  }

  .image-side::before {
    width: 140px;
    height: 140px;
  }

  .image-side img {
    width: 120px;
    height: 120px;
  }
}
</style>
