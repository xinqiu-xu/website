(function () {
  const fallbackLang = "zh";

  function getLang() {
    return localStorage.getItem("lang") || fallbackLang;
  }

  function setLang(lang) {
    localStorage.setItem("lang", lang);
  }

  function getCopy(lang) {
    return window.SITE_CONTENT[lang] || window.SITE_CONTENT[fallbackLang];
  }

  function applyLanguage() {
    const lang = getLang();
    const copy = getCopy(lang);
    document.documentElement.lang = lang === "en" ? "en" : "zh-CN";

    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.dataset.i18n;
      if (copy[key]) {
        el.textContent = copy[key];
      }
    });

    document.querySelectorAll("[data-i18n-html]").forEach((el) => {
      const key = el.dataset.i18nHtml;
      if (copy[key]) {
        el.innerHTML = copy[key];
      }
    });

    document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
      const key = el.dataset.i18nPlaceholder;
      if (copy[key]) {
        el.setAttribute("placeholder", copy[key]);
      }
    });

    document.querySelectorAll("[data-i18n-aria]").forEach((el) => {
      const key = el.dataset.i18nAria;
      if (copy[key]) {
        el.setAttribute("aria-label", copy[key]);
      }
    });

    document.title = document.body.dataset.titleKey ? copy[document.body.dataset.titleKey] : document.title;
  }

  function toggleLang() {
    const next = getLang() === "zh" ? "en" : "zh";
    setLang(next);
    applyLanguage();
  }

  function initModal() {
    const modal = document.querySelector("[data-modal]");
    if (!modal) return;

    const image = modal.querySelector("img");
    const video = modal.querySelector("video");
    const closeButton = modal.querySelector("[data-modal-close]");

    function open(type) {
      modal.classList.add("is-open");
      if (type === "image") {
        image.hidden = false;
        video.hidden = true;
        video.pause();
      } else {
        image.hidden = true;
        video.hidden = false;
        video.currentTime = 0;
        video.play();
      }
      document.body.classList.add("modal-open");
    }

    function close() {
      modal.classList.remove("is-open");
      video.pause();
      video.currentTime = 0;
      document.body.classList.remove("modal-open");
    }

    document.querySelectorAll("[data-open-media]").forEach((button) => {
      button.addEventListener("click", () => open(button.dataset.openMedia));
    });

    closeButton.addEventListener("click", close);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) close();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") close();
    });
  }

  function initNavHighlight() {
    const current = document.body.dataset.page;
    if (!current) return;
    document.querySelectorAll("[data-nav]").forEach((link) => {
      if (link.dataset.nav === current) {
        link.setAttribute("aria-current", "page");
      }
    });
  }

  function initVariantIndex() {
    const list = document.querySelector("[data-variant-list]");
    if (!list) return;
    const lang = getLang();
    const copy = getCopy(lang);
    list.innerHTML = window.SITE_CONTENT.variants.map((variant) => `
      <article class="variant-card variant-card-${variant.id}">
        <p class="variant-chip">${variant.id.toUpperCase()}</p>
        <h2>${copy[variant.keyName]}</h2>
        <p>${copy[variant.keyDesc]}</p>
        <a class="button secondary" href="./${variant.id}/">${copy.variantVisit}</a>
      </article>
    `).join("");
  }

  function boot() {
    applyLanguage();
    initModal();
    initNavHighlight();
    initVariantIndex();
    document.querySelectorAll("[data-toggle-lang]").forEach((button) => {
      button.addEventListener("click", toggleLang);
    });
  }

  window.addEventListener("DOMContentLoaded", boot);
  window.toggleLang = toggleLang;
})();
