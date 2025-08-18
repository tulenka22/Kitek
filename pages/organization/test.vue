<template>
  <block-ab title="В скором времени будет добавлено">
    <div class="container">
      <nav class="menu">
        <h3>Выберите специальность</h3>
        <ul>
          <li
            v-for="(item, index) in professions"
            :key="index"
            :class="{ active: selected === item.name }"
            @click="selected = item.name"
            tabindex="0"
            @keydown.enter="selected = item.name">
            {{ item.name }}
          </li>
        </ul>
      </nav>
      <section class="description">
        <h3>Описание</h3>
        <p v-if="currentProfession">
          {{ currentProfession.description }}
        </p>
        <p v-else>Пожалуйста, выберите специальность слева.</p>
      </section>
    </div>
  </block-ab>
</template>

<script>
export default {
  data() {
    return {
      selected: null,
      professions: [
        {
          name: 'Программист',
          description:
            'Программист разрабатывает и поддерживает программное обеспечение, пишет код и решает технические задачи.',
        },
        {
          name: 'Дизайнер',
          description:
            'Дизайнер создает визуальные концепции, разрабатывает макеты и улучшает пользовательский опыт.',
        },
        {
          name: 'Маркетолог',
          description:
            'Маркетолог анализирует рынок, разрабатывает стратегии продвижения и увеличивает продажи.',
        },
        {
          name: 'Врач',
          description: 'Врач диагностирует и лечит заболевания, заботится о здоровье пациентов.',
        },
        {
          name: 'Учитель',
          description:
            'Учитель обучает и воспитывает учеников, помогает им развиваться и достигать целей.',
        },
      ],
    }
  },
  computed: {
    currentProfession() {
      return this.professions.find((p) => p.name === this.selected)
    },
  },
}
</script>

<style scoped lang="scss">
.container {
  display: flex;
  max-width: 1100px;
  margin: 30px auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

  .menu {
    flex: 1 1 40%;
    background: #007bff;
    color: #fff;
    padding: 20px 25px;

    h3 {
      margin-bottom: 20px;
      font-weight: 700;
      font-size: 1.3rem;
      border-bottom: 2px solid rgba(255, 255, 255, 0.3);
      padding-bottom: 8px;
    }

    ul {
      list-style: none;
      padding: 0;
      margin: 0;

      li {
        cursor: pointer;
        padding: 12px 15px;
        margin-bottom: 10px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.15);
        transition: background-color 0.3s, transform 0.2s;
        user-select: none;

        &:hover,
        &:focus {
          background: rgba(255, 255, 255, 0.3);
          outline: none;
          transform: scale(1.03);
        }

        &.active {
          background: #0056b3;
          font-weight: 700;
          box-shadow: 0 0 8px rgba(0, 86, 179, 0.7);
        }
      }
    }
  }

  .description {
    flex: 1 1 60%;
    padding: 25px 30px;
    color: #333;
    background: #f9f9f9;

    h3 {
      margin-bottom: 20px;
      font-weight: 700;
      font-size: 1.4rem;
      color: #007bff;
      border-bottom: 2px solid #007bff;
      padding-bottom: 8px;
    }

    p {
      font-size: 1.1rem;
      line-height: 1.5;
    }
  }
}

/* Адаптивность */
@media (max-width: 720px) {
  .container {
    flex-direction: column;

    .menu,
    .description {
      flex: none;
      width: 100%;
      padding: 15px 20px;
    }

    .menu {
      h3 {
        font-size: 1.2rem;
      }
      ul li {
        padding: 10px 12px;
        margin-bottom: 8px;
        font-size: 1rem;
      }
    }

    .description {
      h3 {
        font-size: 1.3rem;
      }
      p {
        font-size: 1rem;
      }
    }
  }
}
</style>
