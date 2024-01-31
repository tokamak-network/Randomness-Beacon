import Link from "next/link"

export function NavLink({
    href,
    children,
    target,
}: {
    href: string
    children: React.ReactNode
    target?: string
}) {
    return (
        <Link href={href}>
            <a
                target={target}
                className="inline-block rounded-lg px-2 py-1 text-sm text-slate-700 hover:bg-slate-100 hover:text-slate-900"
            >
                {children}
            </a>
        </Link>
    )
}
