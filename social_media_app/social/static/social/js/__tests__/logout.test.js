/**
 * @jest-environment jsdom
 */
import { setupLogoutButton } from "../logout";

global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
  })
);

describe("logout functionality", () => {
  let originalLocation;

  beforeEach(() => {
    originalLocation = window.location;
    delete window.location;
    window.location = { assign: jest.fn() };

    document.body.innerHTML = `<button id="logout-button">Logout</button>`;
    setupLogoutButton(); // Initialize the logout button
  });

  afterEach(() => {
    window.location = originalLocation;
    jest.clearAllMocks();
  });

  test("should send a logout request and redirect to home", async () => {
    const logoutButton = document.getElementById("logout-button");
    logoutButton.click();

    expect(fetch).toHaveBeenCalledWith("/logout/", { method: "POST" });
    await Promise.resolve();
    expect(window.location.assign).toHaveBeenCalledWith("/");
  });
});