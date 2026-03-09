import CoreGraphics

let args = CommandLine.arguments
let appName = args.count > 1 ? args[1] : ""

let windowList = CGWindowListCopyWindowInfo(.optionOnScreenOnly, kCGNullWindowID) as! [[String: Any]]
for w in windowList {
    if let owner = w["kCGWindowOwnerName"] as? String {
        if appName.isEmpty || owner.lowercased().contains(appName.lowercased()) {
            let id = w["kCGWindowNumber"] as! Int
            let name = w["kCGWindowName"] as? String ?? ""
            let bounds = w["kCGWindowBounds"] as? [String: Any] ?? [:]
            let x = bounds["X"] as? Int ?? 0
            let y = bounds["Y"] as? Int ?? 0
            let width = bounds["Width"] as? Int ?? 0
            let height = bounds["Height"] as? Int ?? 0
            print("\(id)\t\(owner)\t\(name)\t\(x),\(y),\(width),\(height)")
        }
    }
}
