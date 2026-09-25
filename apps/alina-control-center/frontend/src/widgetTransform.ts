export type WidgetId =
  | "KNOWLEDGE"
  | "SOURCES"
  | "PROJECTS"
  | "AGENTS"
  | "WORK_TABLE"
  | "ALINA";

export type WidgetTransform = {
  scale: number;
  x: number;
  y: number;
  minimized: boolean;
  fullscreen: boolean;
  floating: boolean;
};

export const defaultWidgetTransform = (): WidgetTransform => ({
  scale: 1,
  x: 0,
  y: 0,
  minimized: false,
  fullscreen: false,
  floating: false,
});

export const clampWidgetScale = (value: number) =>
  Math.min(5, Math.max(0.5, Number(value.toFixed(2))));

export const zoomWidget = (
  state: WidgetTransform,
  delta: number,
): WidgetTransform => ({
  ...state,
  scale: clampWidgetScale(state.scale + delta),
});

export const moveWidget = (
  state: WidgetTransform,
  x: number,
  y: number,
): WidgetTransform => ({
  ...state,
  x,
  y,
  floating: true,
});

export const toggleWidgetFullscreen = (
  state: WidgetTransform,
): WidgetTransform => ({
  ...state,
  fullscreen: !state.fullscreen,
  minimized: false,
});

export const toggleWidgetMinimized = (
  state: WidgetTransform,
): WidgetTransform => ({
  ...state,
  minimized: !state.minimized,
  fullscreen: false,
});

export const resetWidgetTransform = (): WidgetTransform =>
  defaultWidgetTransform();
