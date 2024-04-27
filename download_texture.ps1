Param(
    [string]$Url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/JPEG_example_flower.jpg/256px-JPEG_example_flower.jpg",
    [string]$Output = "texture.jpg"
)

try {
    Write-Host "Downloading texture from $Url ..."
    Invoke-WebRequest -Uri $Url -OutFile $Output -UseBasicParsing
    Write-Host "Texture saved to $Output"
} catch {
    Write-Error "Failed to download texture: $_"
    exit 1
}
