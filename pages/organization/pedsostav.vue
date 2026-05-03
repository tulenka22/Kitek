<template>
  <block-ab title="Руководство">
    <div class="staff">
      <div v-for="st of staff" :key="st.name" class="staff-card">
        <!-- Фото -->
        <div class="staff-card__photo">
          <img v-if="st.img" :src="st.img" :alt="st.name" class="staff-card__img" />
          <div v-else class="staff-card__placeholder">
            <span class="staff-card__initials">
              {{ getInitials(st.name) }}
            </span>
          </div>
        </div>

        <!-- Информация -->
        <div class="staff-card__content">
          <h3 class="staff-card__name">{{ st.name }}</h3>
          <p class="staff-card__position">{{ st.position }}</p>

          <!-- Контакты с иконками -->
          <div class="staff-card__contacts">
            <div v-if="st.phone" class="staff-card__contact">
              <svg class="staff-card__icon" width="16" height="16" viewBox="0 0 24 24">
                <path
                  d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24 11.36 11.36 0 0 0 3.57.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.36 11.36 0 0 0 .57 3.57 1 1 0 0 1-.25 1.02l-2.2 2.2z"
                  fill="currentColor" />
              </svg>
              <a :href="`tel:${st.phone.replace(/\D/g, '')}`">{{ st.phone }}</a>
            </div>
            <div v-if="st.mail" class="staff-card__contact">
              <svg class="staff-card__icon" width="16" height="16" viewBox="0 0 24 24">
                <path
                  d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zm-2 0l-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z"
                  fill="currentColor" />
              </svg>
              <a :href="`mailto:${st.mail}`">{{ st.mail }}</a>
            </div>
          </div>

          <!-- Кнопка "Подробнее" только при наличии ссылки -->
          <a v-if="st.page" :href="st.page" target="_blank" class="staff-card__more">
            <span>Подробнее</span>
            <svg width="16" height="16" viewBox="0 0 24 24">
              <path
                d="M19 19H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"
                fill="currentColor" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      staff: [
        // ... ваш массив данных без изменений
        {
          name: 'Ивченко Татьяна Павловна',
          position: 'Директор, кандидат педагогических наук, Почетный работник СПО',
          phone: '8 (3812) 68-07-73',
          mail: 'tradeconomy@mail.ru',
          img: '/img/organization/teaching-staff/Татьяна Павловна копия 2.png',
          page: '/organization/Ivchenko-Tatyana-Pavlovna',
        },
        {
          name: 'Стацюк Ольга Валерьевна',
          position: 'Главный бухгалтер',
          phone: '8 (3812) 68-07-64',
          mail: 'tradeconomy@mail.ru',
          img: '',
        },
        {
          name: 'Юрьева Елена Георгиевна',
          position:
            'Заместитель директора по инновационной и проектной деятельности, кандидат педагогических наук',
          phone: '8 (3812) 68-07-82',
          mail: 'tradeconomy@mail.ru',
          img: '/img/organization/teaching-staff/Юрьева Е.Г.png',
        },
        {
          name: 'Загребнев Виталий Юрьевич',
          position: 'Заместитель директора по учебной работе',
          phone: '8 (3812) 68-07-46',
          mail: 'tradeconomy@mail.ru',
          img: '/img/organization/teaching-staff/Загребнев В.Ю.png',
        },
        {
          name: 'Жакенова Айман Оразовна',
          position: 'Заместитель директора по воспитательной работе, кандидат педагогических наук',
          phone: '8 (3812) 68-26-77',
          mail: 'tradeconomy@mail.ru',
          img: '/img/organization/teaching-staff/Жакенова А.О.png',
        },
        {
          name: 'Орлова Вера Михайловна',
          position: 'Заместитель директора по практической подготовке',
          phone: '8 (3812) 68-07-82',
          mail: 'tradeconomy@mail.ru',
          img: '/img/organization/teaching-staff/Орлова В.М.png',
        },
        {
          name: 'Разливинская Марина Васильевна',
          position: 'Заместитель директора по административно-хозяйственной работе',
          phone: '8 (3812) 68-26-55',
          mail: 'tradeconomy@mail.ru',
          img: '',
        },
        {
          name: 'Шевчук Кирилл Александрович',
          position: 'Заместитель директора по вопросам безопасности',
          phone: '8 (3812) 68-07-46',
          mail: 'tradeconomy@mail.ru',
          img: '/img/organization/teaching-staff/Шевчук К.А.png',
        },
      ],
    }
  },
  methods: {
    getInitials(fullName) {
      const parts = fullName.split(' ')
      if (parts.length >= 2) {
        return parts[0][0] + parts[1][0]
      }
      return fullName.substring(0, 2).toUpperCase()
    },
  },
}
</script>

<style scoped lang="scss">
.staff {
  margin-top: 24px;
  display: grid;
  gap: 24px;
  grid-template-columns: repeat(3, 1fr);
  @media screen and (max-width: 1440px) {
    grid-template-columns: repeat(2, 1fr);
  }
  @media screen and (max-width: 640px) {
    grid-template-columns: 1fr;
  }
}

.staff-card {
  display: flex;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
  padding: 20px;
  transition: box-shadow 0.2s ease;
  border: 1px solid #eee;

  &:hover {
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
  }

  &__photo {
    flex-shrink: 0;
    width: 80px;
    height: 100px; // прямоугольная форма
    margin-right: 18px;
    border-radius: 8px; // небольшое скругление углов
    overflow: hidden;
    background: #f5f5f5;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  &__img {
    width: 100%;
    height: 100%;
    object-fit: cover; // изображение заполнит контейнер, сохраняя пропорции
  }

  &__placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(196, 62, 62, 0.08);
  }

  &__initials {
    font-size: 28px;
    font-weight: 500;
    color: #c43e3e;
    text-transform: uppercase;
  }

  &__content {
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  &__name {
    margin: 0 0 6px 0;
    font-size: 18px;
    font-weight: 600;
    line-height: 1.3;
    color: #1a1a1a;
  }

  &__position {
    margin: 0 0 12px 0;
    font-size: 13px;
    line-height: 1.4;
    color: #555;
  }

  &__contacts {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 14px;
  }

  &__contact {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: #666;

    a {
      color: inherit;
      text-decoration: none;
      transition: color 0.15s;

      &:hover {
        color: #c43e3e;
      }
    }
  }

  &__icon {
    flex-shrink: 0;
    color: #c43e3e;
    opacity: 0.8;
  }

  &__more {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    align-self: flex-start;
    margin-top: auto;
    padding: 6px 14px;
    background: transparent;
    border: 1px solid #c43e3e;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 500;
    color: #c43e3e;
    text-decoration: none;
    transition: background 0.2s, color 0.2s;

    svg {
      flex-shrink: 0;
      transition: transform 0.15s;
    }

    &:hover {
      background: #c43e3e;
      color: #fff;

      svg {
        transform: translateX(2px);
        fill: #fff;
      }
    }
  }
}
</style>
