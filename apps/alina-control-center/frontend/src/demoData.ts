import fixture from "../../fixtures/demo-workspace.json";
import type { DemoWorkspace } from "./types";

/**
 * Adapter over the single canonical sanitized DEMO fixture.
 * The JSON file is the source; this module only supplies a typed boundary.
 */
export const demoWorkspace = fixture as DemoWorkspace;
