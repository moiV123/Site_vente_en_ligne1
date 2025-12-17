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
    duration: 0.5,
    onComplete: () => {
      document.getElementById("loader").style.display = "none";
    }
  });
});
