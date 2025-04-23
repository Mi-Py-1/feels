module.exports = {
    collectCoverage: true, // Enable coverage collection
    collectCoverageFrom: [
      "social_media_app/social/static/social/js/**/*.js", // Include all JavaScript files in your project
      "!**/__tests__/**", // Exclude test files
    ],
    coverageDirectory: "coverage", // Directory where coverage reports will be saved
  };