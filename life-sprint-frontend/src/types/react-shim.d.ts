declare namespace JSX {
    interface IntrinsicElements {
        [elemName: string]: any
    }
}

declare module 'react' {
    export type ReactNode = any
    export interface FC<P = {}> {
        (props: P & { children?: ReactNode }): any
    }
    export function useState<S>(
        initialState: S | (() => S)
    ): [S, (value: S | ((prev: S) => S)) => void]
    export function useEffect(effect: () => void | (() => void), deps?: any[]): void
    export function useRef<T>(initialValue: T): { current: T }
}

declare module 'react/jsx-runtime' {
    export const jsx: any
    export const jsxs: any
    export const Fragment: any
}
