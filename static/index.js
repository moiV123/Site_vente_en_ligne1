// Animate the loader
gsap.to("#loader .loader-inner", {
  rotation: 360,
  repeat: -1,
  duration: 1,
  ease: "linear"
});

// Wait for window load
window.addEventListener("load", () => {
  // Animate loader fade out
  gsap.to("#loader", {
    opacity: 0,
    duration: 1,
    onComplete: () => {
      document.getElementById("loader").style.display = "none";
    }
  });
});

// Register ScrollTrigger
gsap.registerPlugin(ScrollTrigger);

// Fade + slide animation for each annonce
gsap.utils.toArray('.scroll-animate').forEach((elem) => {
    gsap.from(elem, {
        scrollTrigger: {
            trigger: elem,
            start: "top 80%", // quand le top de l’élément atteint 80% du viewport
            toggleActions: "play none none none"
        },
        opacity: 0,
        y: 50, // glisse depuis le bas
        duration: 0.8,
        ease: "power2.out",
        stagger: 0.2
    });
});
