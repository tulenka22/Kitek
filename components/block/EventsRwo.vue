<template>
  <div class="my-custom-component">
    <AppBlock title="День открытых дверей">
      <div class="opendoors-banner">
        <!-- Левая часть с текстом -->
        <div class="banner-content">
          <div class="academic-decoration">
            <div class="academic-icon">
              <svg viewBox="0 0 24 24" width="24" height="24">
                <path
                  d="M12 3L1 9l11 6 9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"
                  fill="currentColor" />
              </svg>
            </div>
            <div class="academic-line"></div>
          </div>

          <h2 class="banner-title">
            Приглашаем вас на
            <span class="highlight-text">«Единый День открытых дверей»</span>
          </h2>

          <div class="event-details">
            <div class="detail-item">
              <div class="detail-icon">
                <svg viewBox="0 0 24 24" width="20" height="20">
                  <path
                    d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"
                    fill="currentColor" />
                </svg>
              </div>
              <div class="detail-text">
                <span class="label">Место:</span>
                <span class="value">г. Омск, ул. 27-я Северная, 69</span>
              </div>
            </div>

            <div class="detail-item">
              <div class="detail-icon">
                <svg viewBox="0 0 24 24" width="20" height="20">
                  <path
                    d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z"
                    fill="currentColor" />
                </svg>
              </div>
              <div class="detail-text">
                <span class="label">Дата:</span>
                <span class="value">18 апреля 2026г.</span>
              </div>
            </div>

            <div class="detail-item">
              <div class="detail-icon">
                <svg viewBox="0 0 24 24" width="20" height="20">
                  <path
                    d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"
                    fill="currentColor" />
                </svg>
              </div>
              <div class="detail-text">
                <span class="label">Время:</span>
                <span class="value">10:00</span>
              </div>
            </div>
          </div>

          <div class="invitation-text">
            <p>Для учащихся 8-11 классов, родителей и преподавателей</p>
            <div class="knowledge-icon">
              <svg viewBox="0 0 24 24" width="18" height="18">
                <path
                  d="M12 3L1 9l11 6 9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"
                  fill="currentColor" />
              </svg>
              <span>Откройте мир возможностей</span>
            </div>
          </div>

          <!-- <a href="/data/news/Порядок проведения.pdf" class="info-link" target="_blank">
            <span>Порядок проведения и ФИО кураторов групп</span>
            <svg viewBox="0 0 24 24" width="16" height="16">
              <path
                d="M14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3m-2 16H5V5h7V3H5c-1.11 0-2 .89-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7z"
                fill="currentColor" />
            </svg>
          </a> -->
        </div>

        <!-- Правая часть с изображением -->
        <div class="banner-image">
          <div class="image-container">
            <img
              alt="День открытых дверей"
              src="/img/opendoors/8bmpG1MSlBrz9bjbT0V8gysOLUuutPV06BpZuCru2oxIeNugfiz7rDHWYLyAW5CqC49IVQi7RQkzsOxVrpAqcXq8.jpg"
              class="openDay" />
            <div class="image-overlay">
              <div class="overlay-text">
                <span>Ваше будущее</span>
                <span>начинается здесь</span>
              </div>
            </div>
          </div>
          <div class="image-decoration">
            <div class="decoration-dot"></div>
            <div class="decoration-dot"></div>
            <div class="decoration-dot"></div>
          </div>
        </div>
      </div>
    </AppBlock>
  </div>
</template>

<script>
export default {
  name: 'EventsRwo',
  data() {
    return {
      // ваши данные
    }
  },
  methods: {
    // ваши методы
  },
}
</script>

<style scoped lang="scss">
.block {
  padding-bottom: 0 0 0 0;
}

.my-custom-component {
  margin-bottom: 20px;
}

.opendoors-banner {
  display: flex;
  gap: 40px;

  padding: 40px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  margin: -48px;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #c43e3e, #c43e3e, #c43e3e);
  }
}

.banner-content {
  flex: 1;
  position: relative;
}

.academic-decoration {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 10px;

  .academic-icon {
    width: 50px;
    height: 50px;
    background: linear-gradient(135deg, #c43e3e, #c43e3e);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    box-shadow: 0 4px 12px rgba(44, 82, 130, 0.2);
  }

  .academic-line {
    flex: 1;
    height: 2px;
    background: linear-gradient(90deg, #c43e3e, transparent);
  }
}

.banner-title {
  font-size: 2.2rem;
  font-weight: 700;
  line-height: 1.3;
  color: #1a202c;
  margin-bottom: 30px;

  .highlight-text {
    display: block;
    color: #c43e3e;
    font-size: 2.4rem;
    margin-top: 10px;
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

.event-details {
  background: white;
  border-radius: 16px;
  padding: 25px;
  margin-bottom: 30px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
  border: 1px solid #e2e8f0;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 15px;

  &:last-child {
    margin-bottom: 0;
  }

  .detail-icon {
    width: 40px;
    height: 40px;
    background: #f7fafc;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #c43e3e;
    flex-shrink: 0;
  }

  .detail-text {
    flex: 1;

    .label {
      display: block;
      font-size: 0.9rem;
      color: #718096;
      margin-bottom: 2px;
    }

    .value {
      display: block;
      font-size: 1.1rem;
      font-weight: 600;
      color: #2d3748;
    }
  }
}

.invitation-text {
  margin-bottom: 10px;

  p {
    font-size: 1.1rem;
    color: #4a5568;
    margin-bottom: 15px;
    line-height: 1.5;
  }

  .knowledge-icon {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(44, 82, 130, 0.1);
    padding: 10px 15px;
    border-radius: 10px;
    color: #c43e3e;
    font-weight: 500;

    svg {
      color: #c43e3e;
    }
  }
}

.info-link {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  color: #c43e3e;
  text-decoration: none;
  font-weight: 500;
  padding: 12px 20px;
  background: rgba(44, 82, 130, 0.08);
  border-radius: 10px;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(44, 82, 130, 0.15);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(44, 82, 130, 0.1);
  }

  svg {
    transition: transform 0.3s ease;
  }

  &:hover svg {
    transform: translateX(3px);
  }
}

.banner-image {
  flex: 1;
  position: relative;
}

.image-container {
  position: relative;
  overflow: hidden;
  border-radius: 16px;
  height: 100%;
  min-height: 400px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);

  .openDay {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }

  &:hover .openDay {
    transform: scale(1.03);
  }
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent);
  padding: 30px;
  color: white;

  .overlay-text {
    font-size: 1.4rem;
    font-weight: 600;
    display: flex;
    flex-direction: column;
    line-height: 1.4;

    span {
      &:first-child {
        color: #c43e3e;
      }
    }
  }
}

.image-decoration {
  position: absolute;
  top: 20px;
  right: -10px;
  display: flex;
  flex-direction: column;
  gap: 8px;

  .decoration-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #c43e3e;

    &:nth-child(2) {
      background: #c43e3e;
    }

    &:nth-child(3) {
      background: #c43e3e;
    }
  }
}

// Адаптивность
@media (max-width: 992px) {
  .opendoors-banner {
    flex-direction: column;
    gap: 30px;
  }

  .banner-title {
    font-size: 1.8rem;

    .highlight-text {
      font-size: 2rem;
    }
  }

  .image-container {
    min-height: auto;
  }
}

@media (max-width: 576px) {
  .opendoors-banner {
    padding: 10px;
  }

  .banner-title {
    font-size: 1.5rem;

    .highlight-text {
      font-size: 1.7rem;
    }
  }

  .event-details {
    padding: 20px;
  }

  .detail-item {
    align-items: flex-start;
    gap: 8px;

    .detail-icon {
      align-self: flex-start;
    }
  }
}
</style>
