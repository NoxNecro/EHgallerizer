$targetSize = 10MB
$frameRate = 15

Get-ChildItem -Filter *.gif | ForEach-Object {
    $file = $_.FullName

    # Check if file is already under 10MB
    if ((Get-Item "$file").Length -le $targetSize) {
        Write-Host "Skipping $file (already under 10MB)"
        return
    }

    $outputFile = "compressed_$($_.Name)"

    # Capture ffmpeg output
    $ffmpegOutput = ffmpeg -i "$file" 2>&1 | Out-String
    $dimensions = $ffmpegOutput | Select-String -Pattern "\d{2,4}x\d{2,4}" | Select-Object -First 1

    if ($dimensions -match "(\d+)x(\d+)") {
        $width = [int]$matches[1]
        $height = [int]$matches[2]
    } else {
        Write-Host "Skipping $file (unable to determine dimensions)"
        return
    }

    # Initial scale factor
    $scaleFactor = 0.8

    while ($true) {
        $newWidth = [math]::Floor($width * $scaleFactor)
        $newHeight = [math]::Floor($height * $scaleFactor)

        # Update ffmpeg command to try different dithering and palette options
        ffmpeg -y -i "$file" -vf "scale=${newWidth}:${newHeight},split [a][b];[a] palettegen=max_colors=256 [p];[b][p] paletteuse=dither=bayer" -r $frameRate "$outputFile"

        # Check if the compressed file is under target size
        if ((Get-Item "$outputFile").Length -le $targetSize) {
            Write-Host "Compressed $file to under 10MB"
            
            # Delete the original file
            Remove-Item "$file"

            # Rename the compressed file to the original filename
            Rename-Item "$outputFile" -NewName "$($_.Name)"
            Write-Host "Renamed compressed file to $($_.Name)"
            break
        }

        # Decrease scale factor if file is still too large
        $scaleFactor *= 0.9
        if ($scaleFactor -lt 0.1) {
            Write-Host "Cannot compress $file below 10MB without extreme quality loss"
            break
        }
    }
}
