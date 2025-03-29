(function () {
  "use strict";

  // ======================
  // Dropdown Menu Toggler for Mobile
  // ======================
  const dropdownMenuToggler = document.querySelectorAll(".nav-dropdown > .nav-link");
  dropdownMenuToggler.forEach((toggler) => {
    toggler?.addEventListener("click", (e) => {
      e.target.closest(".nav-item").classList.toggle("active");
    });
  });

  // ======================
  // Testimonial Slider Configuration
  // ======================
  const testimonialSlider = new Swiper(".testimonial-slider", {
    spaceBetween: 24,
    loop: true,
    pagination: {
      el: ".testimonial-slider-pagination",
      type: "bullets",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      768: { slidesPerView: 2 },
      992: { slidesPerView: 3 },
    },
  });

  // ======================
  // Swiper Navigation Buttons Styling
  // ======================
  const swiperStyle = document.createElement("style");
  swiperStyle.innerHTML = `
    .swiper-button-next, .swiper-button-prev {
      width: 30px;
      height: 30px;
    }
    .swiper-button-next::after, .swiper-button-prev::after {
      font-size: 25px !important;
    }
    body:not(.dark) .swiper-button-next,
    body:not(.dark) .swiper-button-prev {
      color: rgb(0, 0, 0) !important;
    }
    body.dark .swiper-button-next,
    body.dark .swiper-button-prev {
      color: rgb(255, 255, 255) !important;
    }
  `;
  document.head.appendChild(swiperStyle);

  // ======================
  // Accordion Functionality
  // ======================
  document.querySelectorAll(".accordion-header").forEach((button) => {
    button.addEventListener("click", function () {
      const content = this.nextElementSibling;
      const isActive = this.classList.contains("active");

      // Close all other accordions
      document.querySelectorAll(".accordion-header").forEach((btn) => {
        btn.classList.remove("active");
      });
      document.querySelectorAll(".accordion-content").forEach((content) => {
        content.style.maxHeight = null;
      });

      // Toggle current accordion
      if (!isActive) {
        this.classList.add("active");
        content.style.maxHeight = `${content.scrollHeight}px`;
      }
    });
  });
})();