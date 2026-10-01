/* Sabiha Tex & Apparels — small progressive enhancements */
(function () {
  "use strict";

  // mobile navigation
  var burger = document.querySelector(".burger");
  var nav = document.querySelector("nav.main");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      }
    });
  }

  // current year in footer
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  // reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if (items.length) {
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
      items.forEach(function (el) { io.observe(el); });
    }
  }

  // enquiry form -> opens the visitor's mail app with the message prefilled
  var form = document.querySelector("form.enquiry");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = function (n) { var el = form.querySelector('[name="' + n + '"]'); return el ? el.value.trim() : ""; };
      var subject = "Sourcing enquiry — " + (f("company") || f("name") || "new enquiry");
      var body = [
        "Name: " + f("name"),
        "Company: " + f("company"),
        "Email: " + f("email"),
        "Phone: " + f("phone"),
        "Country: " + f("country"),
        "Product category: " + f("category"),
        "",
        "Details:",
        f("message")
      ].join("\n");
      var status = form.querySelector(".form-note");
      if (status) status.textContent = "Opening your email app… if nothing happens, write to smtsajib25@gmail.com.";
      window.location.href = "mailto:smtsajib25@gmail.com?subject=" +
        encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
    });
  }
})();
