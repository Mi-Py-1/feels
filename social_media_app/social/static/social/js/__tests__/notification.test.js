/**
 * @jest-environment jsdom
 */
import { fetchNotifications } from "../notifications";

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () =>
      Promise.resolve({
        notifications: [
          { message: "New post created!", tag: "success" },
          { message: "You have a new feel!", tag: "info" },
        ],
      }),
  })
);

describe("fetchNotifications", () => {
  beforeEach(() => {
    document.body.innerHTML = `<div id="notifications"></div>`;
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test("should fetch notifications and update the DOM", async () => {
    await fetchNotifications();

    // Wait for the DOM updates to complete
    await new Promise((resolve) => setTimeout(resolve, 0));

    const notificationsDiv = document.getElementById("notifications");
    expect(notificationsDiv.children.length).toBe(2); // Ensure two notifications are added
    expect(notificationsDiv.children[0].textContent).toContain("New post created!");
    expect(notificationsDiv.children[1].textContent).toContain("You have a new feel!");
  });
});