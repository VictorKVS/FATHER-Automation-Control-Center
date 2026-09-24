import { describe, expect, it } from "vitest";
import {
  defaultWidgetTransform,
  moveWidget,
  resetWidgetTransform,
  toggleWidgetFullscreen,
  toggleWidgetMinimized,
  zoomWidget,
} from "./widgetTransform";

describe("Adaptive Workspace WidgetTransform", () => {
  it("keeps each widget transform independent", () => {
    const knowledge = zoomWidget(defaultWidgetTransform(), 1);
    const alina = defaultWidgetTransform();
    expect(knowledge.scale).toBe(2);
    expect(alina.scale).toBe(1);
  });

  it("clamps zoom to safe presentation limits", () => {
    expect(zoomWidget(defaultWidgetTransform(), 20).scale).toBe(5);
    expect(zoomWidget(defaultWidgetTransform(), -20).scale).toBe(0.5);
  });

  it("moving a widget promotes it to floating presentation state", () => {
    const moved = moveWidget(defaultWidgetTransform(), 120, -40);
    expect(moved).toMatchObject({ x: 120, y: -40, floating: true });
  });

  it("fullscreen and minimized are mutually exclusive", () => {
    const minimized = toggleWidgetMinimized(defaultWidgetTransform());
    const fullscreen = toggleWidgetFullscreen(minimized);
    expect(fullscreen.fullscreen).toBe(true);
    expect(fullscreen.minimized).toBe(false);
  });

  it("reset returns the canonical presentation defaults", () => {
    const changed = moveWidget(zoomWidget(defaultWidgetTransform(), 2), 50, 80);
    expect(resetWidgetTransform()).toEqual(defaultWidgetTransform());
    expect(changed).not.toEqual(resetWidgetTransform());
  });
});
