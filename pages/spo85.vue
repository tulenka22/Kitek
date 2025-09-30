<template>
  <block-ab title="85 лет системе СПО">
    <div class="anniversary-block">
      <h2 class="anniversary-title">Всероссийская акция «СПО-гордость страны!»</h2>

      <div class="video-wrapper">
        <div class="video-container">
          <video class="ab__video" controls poster="/video-poster.jpg">
            <source src="/video/prepod99.mp4" type="video/mp4" />
            Ваш браузер не поддерживает видео
          </video>
          <div class="video-overlay">
            <button class="play-button" aria-label="Воспроизвести видео">
              <svg
                width="64"
                height="64"
                viewBox="0 0 64 64"
                fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <circle cx="32" cy="32" r="32" fill="white" fill-opacity="0.9" />
                <path d="M42 32L26 40V24L42 32Z" fill="#3498db" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div class="video-caption">
        <p class="ab__p">
          <span class="icon-container">
            <svg
              class="icon-person"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="7" r="5" />
              <path
                d="M17 14H17.3517C18.8646 14 20.1408 15.1266 20.3285 16.6279L20.719 19.7519C20.8682 20.9456 19.9374 22 18.7344 22H5.26556C4.06257 22 3.1318 20.9456 3.28101 19.7519L3.67151 16.6279C3.85917 15.1266 5.13538 14 6.64835 14H7"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </span>
          <span class="text-prepod"><b>Ли А. А.</b> выпускница 2004г.</span>
        </p>
      </div>

      <div class="video-wrapper">
        <div class="video-container">
          <video class="ab__video" controls poster="/video-poster.jpg">
            <source src="/video/prepod123456789.mp4" type="video/mp4" />
            Ваш браузер не поддерживает видео
          </video>
          <div class="video-overlay">
            <button class="play-button" aria-label="Воспроизвести видео">
              <svg
                width="64"
                height="64"
                viewBox="0 0 64 64"
                fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <circle cx="32" cy="32" r="32" fill="white" fill-opacity="0.9" />
                <path d="M42 32L26 40V24L42 32Z" fill="#3498db" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div class="video-caption">
        <p class="ab__p">
          <span class="icon-container">
            <svg
              class="icon-person"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="7" r="5" />
              <path
                d="M17 14H17.3517C18.8646 14 20.1408 15.1266 20.3285 16.6279L20.719 19.7519C20.8682 20.9456 19.9374 22 18.7344 22H5.26556C4.06257 22 3.1318 20.9456 3.28101 19.7519L3.67151 16.6279C3.85917 15.1266 5.13538 14 6.64835 14H7"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </span>
          <span class="text-prepod"
            ><b>Павленко А.В.</b> зав.отделением, преподаватель , выпускница колледжа 2007г.</span
          >
        </p>
      </div>

      <div class="video-wrapper">
        <div class="video-container">
          <video class="ab__video" controls poster="/video-poster.jpg">
            <source src="/video/prepodkol.mp4" type="video/mp4" />
            Ваш браузер не поддерживает видео
          </video>
          <div class="video-overlay">
            <button class="play-button" aria-label="Воспроизвести видео">
              <svg
                width="64"
                height="64"
                viewBox="0 0 64 64"
                fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <circle cx="32" cy="32" r="32" fill="white" fill-opacity="0.9" />
                <path d="M42 32L26 40V24L42 32Z" fill="#3498db" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div class="video-caption">
        <p class="ab__p">
          <span class="icon-container">
            <svg
              class="icon-person"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="7" r="5" />
              <path
                d="M17 14H17.3517C18.8646 14 20.1408 15.1266 20.3285 16.6279L20.719 19.7519C20.8682 20.9456 19.9374 22 18.7344 22H5.26556C4.06257 22 3.1318 20.9456 3.28101 19.7519L3.67151 16.6279C3.85917 15.1266 5.13538 14 6.64835 14H7"
                stroke-linecap="round"
                stroke-linejoin="round" />
            </svg>
          </span>
          <span class="text-prepod"
            ><b>Колиева М.А. </b>зав.отделением, преподаватель , выпускница колледжа 2004г.</span
          >
        </p>
      </div>
    </div>
  </block-ab>
</template>

<style scoped>
.text-prepod {
  font-size: 24px;
}
.anniversary-block {
  max-width: 800px;

  padding: 25px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
}

.anniversary-title {
  font-size: 28px;
  color: #2c3e50;
  margin-bottom: 25px;
  font-weight: 700;
  line-height: 1.3;
  text-align: center;
}

.video-wrapper {
  position: relative;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  margin-bottom: 20px;
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
  object-fit: cover;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.05);
  transition: opacity 0.3s ease;
  pointer-events: none;
}

.ab__video::-webkit-media-controls-panel {
  background: rgba(0, 0, 0, 0.7);
}

.ab__video::-webkit-media-controls-play-button,
.ab__video::-webkit-media-controls-volume-slider,
.ab__video::-webkit-media-controls-timeline {
  filter: invert(1);
}

.play-button {
  pointer-events: auto;
  cursor: pointer;
  background: none;
  border: none;
  opacity: 0.9;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.play-button:hover {
  transform: scale(1.1);
  opacity: 1;
}

.video-caption {
  text-align: center;
  padding: 15px 0;
}

.ab__p {
  display: flex;
  align-items: center;
  padding-left: 15px;
  font-size: 18px;
  color: #2c3e50;
  margin: 0;
  line-height: 1.5;
  gap: 10px;
}

.ab__p b {
  color: #3498db;
  font-weight: 600;
}

.icon-container {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  background: #f0f8ff;
  border-radius: 50%;
  padding: 5px;
}

.icon-person {
  width: 100%;
  height: 100%;
  color: #3498db;
}

.icon-person circle {
  stroke: currentColor;
  fill: white;
  stroke-width: 2;
}

.icon-person path {
  stroke: currentColor;
  fill: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

/* Анимация загрузки */
@keyframes pulse {
  0% {
    opacity: 0.6;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0.6;
  }
}

.video-wrapper.loading .video-overlay {
  animation: pulse 1.5s infinite;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .anniversary-block {
    padding: 18px;
  }

  .anniversary-title {
    font-size: 23px;
    margin-bottom: 20px;
  }

  .video-wrapper {
    border-radius: 8px;
  }

  .ab__p {
    font-size: 16px;
  }

  .play-button svg {
    width: 56px;
    height: 56px;
  }

  .icon-container {
    width: 24px;
    height: 24px;
  }
}

@media (max-width: 480px) {
  .anniversary-title {
    font-size: 21px;
  }

  .ab__p {
    font-size: 15px;
    flex-direction: column;
    gap: 5px;
  }

  .play-button svg {
    width: 48px;
    height: 48px;
  }

  .icon-container {
    width: 22px;
    height: 22px;
  }
}
</style>

<script>
export default {
  mounted() {
    // Добавляем обработчик для скрытия overlay при воспроизведении
    const video = this.$el.querySelector('.ab__video')
    const overlay = this.$el.querySelector('.video-overlay')

    if (video && overlay) {
      video.addEventListener('play', () => {
        overlay.style.opacity = '0'
        setTimeout(() => {
          overlay.style.display = 'none'
        }, 300)
      })

      video.addEventListener('pause', () => {
        overlay.style.display = 'flex'
        setTimeout(() => {
          overlay.style.opacity = '1'
        }, 10)
      })
    }
  },
}
</script>
